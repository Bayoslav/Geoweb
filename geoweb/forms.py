from django import forms


class GeoFeatureFileForm(forms.Form):
    geo_features = forms.FileField()
    to_json = forms.BooleanField(required=False)
    to_shp = forms.BooleanField(required=False)
