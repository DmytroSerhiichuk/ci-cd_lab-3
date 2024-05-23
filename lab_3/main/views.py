from django.shortcuts import render, redirect
from .models import Category, Product, Brand
from django.contrib.auth import authenticate, login as auth_login
from .forms import SignupForm, AuthenticationForm

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

def profile(request):
    if request.user.is_authenticated:
        data = {
            'title': 'Amado - Furniture Ecommerce Template | Home',
        }
        return render(request, 'index.html', context=data)
    else:
        return redirect('login')
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    data = {
        'title': 'Amado - Furniture Ecommerce Template | LogIn',
        'form': form
    }

    print(form)

    return render(request, 'login.html', context=data)  
    
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignupForm()

    data = {
        'title': 'Amado - Furniture Ecommerce Template | SignUp',
        'form': form
    }

    return render(request, 'signup.html', context=data)    