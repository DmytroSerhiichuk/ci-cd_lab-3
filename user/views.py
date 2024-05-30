from django.shortcuts import render, redirect
from .forms import UserUpdateForm, SignupForm
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

# Create your views here.

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
        return redirect('user:login')
    
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
        return redirect('user:login')
    
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('main:home')
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('user:profile')
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
            return redirect('user:profile')
    else:
        form = SignupForm()

    data = {
        'title': 'Amado - Furniture Ecommerce Template | Sign Up',
        'form': form
    }

    return render(request, 'signup.html', context=data)    