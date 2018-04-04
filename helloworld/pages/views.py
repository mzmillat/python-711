from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def home_new(request):
#     return HttpResponse("Hello world this is pages")

class Home_New(TemplateView):
    template_name ='index.html'

class AboutPageView(TemplateView):
    template_name ='index.html'