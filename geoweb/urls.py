from django.urls import include, path
from geoweb.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]