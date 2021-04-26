from django.urls import include, path
from geoweb.views import IndexView, GenerateReportView

urlpatterns = [
    path('', IndexView.as_view()),
]