from django import forms


class GeoFeatureFileForm(forms.Form):
    file = forms.FileField()
    to_json = forms.BooleanField(required=False)
    to_shp = forms.BooleanField(required=False)
