from django import forms

class GeoFeatureFileForm(forms.Form):
    geo_features = forms.FileField()