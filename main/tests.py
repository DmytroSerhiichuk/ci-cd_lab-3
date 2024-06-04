from django.test import TestCase
from django.urls import reverse
from .models import Category, Brand, Product
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class MainTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category 1', 
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'))
        self.brand = Brand.objects.create(name='Test Brand 1')
        self.product = Product.objects.create(name='Test Product 1', category=self.category, brand=self.brand, price=100, 
                               image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'))

    def test_category_link(self):
        self.assertEqual(self.category.link, 'test-category-1')

    def test_product_view_status_code(self):
        response = self.client.get(reverse('main:product', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)

    def test_category_view_context_data(self):
        response = self.client.get(reverse('main:category', args=[self.category.link]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['brands'][0].name, self.brand.name)
        self.assertEqual(response.context['products'][0].name, self.product.name)