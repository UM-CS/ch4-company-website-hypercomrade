# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context

# NEW: Products page view
class ProductsPageView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add 4 products to the context
        context["products"] = [
            {"name": "Laptop", "price": "$999", "description": "High-performance laptop"},
            {"name": "Mouse", "price": "$25", "description": "Wireless optical mouse"},
            {"name": "Keyboard", "price": "$75", "description": "Mechanical keyboard"},
            {"name": "Monitor", "price": "$300", "description": "27-inch 4K display"},
        ]
        return context
