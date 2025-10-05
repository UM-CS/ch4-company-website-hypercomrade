# pages/urls.py
from django.urls import path
from .views import home_page_view, AboutPageView, ProductsPageView  # updated

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("products/", ProductsPageView.as_view(), name="products"),  # new
    path("", home_page_view, name="home"),
]
