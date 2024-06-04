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

    selectedBrandsNames = request.GET.getlist('brand', [])
    if selectedBrandsNames == []:
        selectedBrands = Brand.objects.all()
    else:
        selectedBrands = Brand.objects.filter(name__in=selectedBrandsNames)
    min_price = request.GET.get('min-price', 10)
    max_price = request.GET.get('max-price', 500)

    data = {
        'title': 'Amado - Furniture Ecommerce Template | Shop',
        'category_name': category.name,
        'products': Product.objects.filter(category=category, price__gte=min_price, price__lte=max_price, brand__in=selectedBrands),
        'brands': Brand.objects.all(),
        'selectedBrands': selectedBrandsNames,
        'min_price': min_price,
        'max_price': max_price
    }

    return render(request, 'category.html', context=data)

def product(request, pk):
    product_obj = Product.objects.get(pk=pk)

    data = {
        'title': 'Amado - Furniture Ecommerce Template | Product',
        'product': product_obj
    }

    return render(request, 'product.html', context=data)

