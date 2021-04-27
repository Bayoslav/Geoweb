import datetime
from zipfile import ZipFile

from django.templatetags.static import static

import geopandas as gpd
from django.conf import settings
from django.shortcuts import render
from django.http import FileResponse
from rest_framework.views import APIView, Response
from rest_framework.response import Response


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
        file_type = "shp"  # https://gis.stackexchange.com/questions/317714/creating-a-shapefile-within-a-zip-file-with-fiona
        kwargs = {}
        current_datetime = datetime.datetime.now()
        prefix = ""

        if getattr(request.POST, "to_json"):
            file_type = "json"
            kwargs["driver"] = "GeoJSON"

        name = f"{current_datetime}." + file_type
        full_name = "api/static/" + name

        data.to_file(full_name, **kwargs)

        return Response({"url": static(name)})