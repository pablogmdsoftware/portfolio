from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="root"),
    path("home/", views.home, name="home"),
    path("projects/data-analysis/", views.data_analysis, name="data_analysis"),
    path("projects/data-science/", views.data_science, name="data_science"),
    path("projects/web-development/", views.web_development, name="web_development"),
]