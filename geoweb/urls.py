from django.urls import path

from geoweb.views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]
