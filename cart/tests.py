from django.test import TestCase
from django.urls import reverse
from .models import Cart
from main.models import Category, Brand, Product
from user.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class CartTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category 1', 
            image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'))
        self.brand = Brand.objects.create(name='Test Brand 1')
        self.product = Product.objects.create(name='Test Product 1', category=self.category, brand=self.brand, price=100, 
                               image=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'))
        
        self.user = User.objects.create_user(email='test@test.com', password='111')
        self.client.login(email='test@test.com', password='111')

        self.cart = Cart.objects.create(user=self.user, product=self.product, count=3)

    def test_cart_view_context_data(self):
        response = self.client.get(reverse('cart:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['items'][0].product, self.product)
        self.assertEqual(response.context['total_price'], self.product.price * 3)