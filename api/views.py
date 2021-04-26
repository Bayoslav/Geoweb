import geopandas as gpd
from django.shortcuts import render
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
