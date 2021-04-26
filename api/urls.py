from django.urls import include, path
from api.views import GenerateReportView

urlpatterns = [
    path('generate-report', GenerateReportView.as_view(), name="generate-report")
]