from django.shortcuts import render
from .projects import WEB_DEVELOPMENT

def home(request):
    context = {}
    return render(request, "app/home.html", context)

def data_analysis(request):
    context = {}
    return render(request, "app/data_analysis.html", context)

def data_science(request):
    context = {}
    return render(request, "app/data_science.html", context)

def web_development(request):
    context = {"projects": WEB_DEVELOPMENT}
    return render(request, "app/web_development.html", context)

def bus_system(request):
    context = {"collection":"web_development"}
    return render(request, "app/projects/bus_system.html", context)