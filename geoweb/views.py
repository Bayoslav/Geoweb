from django.shortcuts import render
from geoweb.forms import GeoFeatureFileForm

from django.views import View


class IndexView(View):

    def get(self, request):

        form = GeoFeatureFileForm()
        return render(request, "index.html", {"form": form})
