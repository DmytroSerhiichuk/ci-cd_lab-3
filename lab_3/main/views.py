from django.shortcuts import render, redirect
from .models import Category, Product, Brand
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import SignupForm, AuthenticationForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm

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
        form = UserUpdateForm(instance=request.user)
        if request.method == "POST":
            form = UserUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
        data = {
            'title': 'Amado - Furniture Ecommerce Template | Profile',
            'user': request.user,
            'form': form
        }
        return render(request, 'profile.html', context=data)
    else:
        return redirect('login')
    
def password_change(request):
    if request.user.is_authenticated:
        form = PasswordChangeForm(request.user)
        if request.method == "POST":
            form = PasswordChangeForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
        data = {
            'title': 'Amado - Furniture Ecommerce Template | Password Changing',
            'user': request.user,
            'form': form
        }
        return render(request, 'password_change.html', context=data)
    else:
        return redirect('login')
    
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('home')
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()

    data = {
        'title': 'Amado - Furniture Ecommerce Template | Log In',
        'form': form
    }

    return render(request, 'login.html', context=data)  
    
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()

    data = {
        'title': 'Amado - Furniture Ecommerce Template | Sign Up',
        'form': form
    }

    return render(request, 'signup.html', context=data)    