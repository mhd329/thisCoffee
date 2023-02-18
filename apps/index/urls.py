from django.urls import path
from . import views

app_name = "apps.index"

urlpatterns = [
    path("", views.index, name="index"),
]
