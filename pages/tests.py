# pages/tests.py
from django.test import TestCase
from django.urls import reverse
from .views import ProductsPageView

class ProductsPageTests(TestCase):

    def test_products_url_exists_at_correct_location(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)

    def test_products_url_available_by_name(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)

    def test_products_template_name_correct(self):
        response = self.client.get(reverse("products"))
        self.assertTemplateUsed(response, "products.html")

    def test_products_template_content(self):
        response = self.client.get(reverse("products"))
        self.assertContains(response, "Our Products")
        self.assertContains(response, "Laptop")
        self.assertContains(response, "Mouse")

    def test_products_context_data(self):
        response = self.client.get(reverse("products"))
        # Check that products context exists
        self.assertTrue('products' in response.context)
        # Check that we have 4 products
        self.assertEqual(len(response.context['products']), 4)
        # Check product data
        products = response.context['products']
        self.assertEqual(products[0]['name'], 'Laptop')
        self.assertEqual(products[1]['price'], '$25')

    def test_products_page_extends_base_template(self):
        response = self.client.get(reverse("products"))
        self.assertContains(response, 'href="/"')  # Check for home link
        self.assertContains(response, 'href="/about/"')  # Check for about link
        self.assertContains(response, 'href="/products/"')  # Check for products link
