from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="root"),
    path("home/", views.home, name="home"),
    path("data-analysis/", views.data_analysis, name="data_analysis"),
    path("data-science/", views.data_science, name="data_science"),
    path("web-development/", views.web_development, name="web_development"),
    path("web-development/bus_system/", views.bus_system, name="bus_system"),
]