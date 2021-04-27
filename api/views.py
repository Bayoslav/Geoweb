
import geopandas as gpd
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.utils import convert_to_format


class GenerateReportView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        data = gpd.read_file(request.FILES["file"])
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
    parser_classes = [JSONParser, FileUploadParser]

    def post(self, request, format=None):
        file = request.FILES["file"]
        convert_to = "shp"
        if "to_json" in request.POST.keys():
            convert_to = "json"
        url = convert_to_format(file, convert_to)
        # https://gis.stackexchange.com/questions/317714/creating-a-shapefile-within-a-zip-file-with-fiona
        return Response({"url": url})


class ConvertFileAjaxView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        file = request.FILES["file"]
        convert_to = "shp"
        if "to_json" in request.POST.keys():
            convert_to = "json"
        url = convert_to_format(file, convert_to)
        return Response({"url": url})
