from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from api.views import ConvertFileAjaxView, ConvertFileView, GenerateReportView

urlpatterns = [
    path('generate-report', GenerateReportView.as_view(),
         name="generate-report"),
    path('convert-file', ConvertFileView.as_view(),
         name="convert-file"),
    path('convert-file-ajax', ConvertFileAjaxView.as_view(),
         name="convert-file-ajax")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
