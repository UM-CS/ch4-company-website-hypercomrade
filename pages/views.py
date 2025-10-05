# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    return render(request, "home.html")

class AboutPageView(TemplateView):
    template_name = "about.html"
