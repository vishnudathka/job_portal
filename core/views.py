from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic as views

class Homeview(views.TemplateView):
    template_name= "core/home.html"

# Create your views here.
