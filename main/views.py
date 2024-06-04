from django.shortcuts import render
from .models import *
import json

# Create your views here.

def index(request):
    user_type = 'registred' if request.user.is_authenticated else 'guest'
    print(user_type)
    product = Product.objects.all()
    data = {
        'title': 'Amado - Furniture Ecommerce Template | Home',
        'products': product,
        'user_type': user_type
    }
    return render(request, 'index.html', context=data)

def shop(request):
    user_type = 'registred' if request.user.is_authenticated else 'guest'
    product = Product.objects.all()
    data = {
        'title': 'Amado - Furniture Ecommerce Template | Shop',
        'categories': Category.objects.all(),
        'products': product,
        'user_type': user_type
    }
    return render(request, 'shop.html', context=data)

def category(request, category_link):
    category = Category.objects.get(link=category_link)

    selectedBrands = request.GET.getlist('brand', [])
    min_price = request.GET.get('min-price', 10)
    max_price = request.GET.get('max-price', 500)

    data = {
        'categories': Category.objects.all(),
        'title': 'Amado - Furniture Ecommerce Template | Shop',
        'category_name': category.name,
        'products': Product.objects.filter(category=category),
        'brands': Brand.objects.all(),
        'selectedBrands': selectedBrands,
        'min_price': min_price,
        'max_price': max_price
    }
    return render(request, 'category.html', context=data)

def product(request, product_link):
    # product = Product.objects.get(link=product_link)
    product = {
        'name': 'hhh'
    }

    data = {
        'title': product.name,
        'product': product
    }
    return render(request, 'product.html', context=data)

def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    quantity = data['quantity'] 
    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=customer, complete=False)

    orderItem, created = PurchaseItem.objects.get_or_create(order=order, movie=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + quantity)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - quantity)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
