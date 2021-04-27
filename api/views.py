import datetime
import shutil
from zipfile import ZipFile

import geopandas as gpd
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from django.templatetags.static import static
from rest_framework.response import Response
from rest_framework.views import APIView, Response


class GenerateReportView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        data = gpd.read_file(request.FILES["geo_features"])
        resp = {}
        if data.geom_type.any() == "Point":
            resp["boundary_box"] = data.total_bounds
        elif data.geom_type.any() == "LineString":
            data.to_crs(epsg=3310, inplace=True)  # use meters
            resp["max_line"] = data.length.max()
            resp["min_line"] = data.length.min()
        else:
            data.to_crs(epsg=3310, inplace=True)
            resp["max_polygon_area"] = data.area.max()
            resp["min_polygon_area"] = data.area.min()
        resp["row_length"] = len(data)
        return Response(resp)


class ConvertFileView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        data = gpd.read_file(request.FILES["geo_features"])
        # https://gis.stackexchange.com/questions/317714/creating-a-shapefile-within-a-zip-file-with-fiona
        file_type = "folder"
        kwargs = {}
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        if "to_json" in request.POST.keys() and request.POST["to_json"]:
            file_type = "json"
            kwargs["driver"] = "GeoJSON"

        name = f"{current_datetime}." + file_type
        full_name = "api/static/" + name
        data.to_file(full_name, **kwargs)
        if file_type == "folder":
            name = f"{current_datetime}.zip"
            filename = shutil.make_archive(
                f"api/static/{current_datetime}", 'zip', full_name)
            # Delete a folder after it's been zipped
            shutil.rmtree(f"{full_name}")
        return Response({"url": static(name)})
