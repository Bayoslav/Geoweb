from django.shortcuts import render
from django.views import View

from geoweb.forms import GeoFeatureFileForm


class IndexView(View):

    def get(self, request):

        form = GeoFeatureFileForm()
        return render(request, "index.html", {"form": form, "url": ""})
