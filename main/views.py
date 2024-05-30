from django.shortcuts import render
from .models import Category, Product, Brand

# Create your views here.

def index(request):
    data = {
        'title': 'Amado - Furniture Ecommerce Template | Home',
    }
    return render(request, 'index.html', context=data)

def shop(request):
    data = {
        'title': 'Amado - Furniture Ecommerce Template | Shop',
        'categories': Category.objects.all(),
    }
    return render(request, 'shop.html', context=data)

def category(request, category_link):
    category = Category.objects.get(link=category_link)

    selectedBrands = request.GET.getlist('brand', [])
    min_price = request.GET.get('min-price', 10)
    max_price = request.GET.get('max-price', 500)

    data = {
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
