from django.conf import settings
from django.urls import include, path
from api.views import GenerateReportView, ConvertFileView
from django.conf.urls.static import static

urlpatterns = [
    path('generate-report', GenerateReportView.as_view(), name="generate-report"),
    path('convert-file', ConvertFileView.as_view(), name="convert-file")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
