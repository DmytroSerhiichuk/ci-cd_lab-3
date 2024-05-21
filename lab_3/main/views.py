from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def index(request):
    data = {
        'title': 'Home',
    }
    return render(request, 'index.html', context=data)

def categories(request):
    data = {
        'title': 'Categories',
        'categories': Category.objects.all()
    }
    return render(request, 'categories.html', context=data)

def category(request, category_link):
    category = Category.objects.get(link=category_link)

    data = {
        'title': category.name,
        'products': Product.objects.filter(category=category)
    }
    return render(request, 'category.html', context=data)

def product(request, product_link):
    product = Product.objects.get(link=product_link)

    data = {
        'title': product.name,
        'product': product
    }
    return render(request, 'product.html', context=data)