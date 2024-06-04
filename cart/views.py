from django.shortcuts import render, redirect
from .models import Cart
from main.models import Product

# Create your views here.

def index(request):
    if request.user.is_authenticated:

        items = Cart.objects.filter(user=request.user)
        
        total_price = 0
        for item in items:
            total_price += item.product.price * item.count

        data = {
            'title': 'Amado - Furniture Ecommerce Template | Cart',
            'items': items,
            'total_price': total_price
        }
        return render(request, 'cart.html', context=data)
    redirect('user:login')

def add(request):
    if request.user.is_authenticated:
        product_id = request.GET.get('pk', -1)
        count = request.GET.get('count', 1)

        product = Product.objects.get(pk=product_id)

        try:
            cart = Cart.objects.get(user=request.user, product=product)
            cart.count = count
        except:
            cart = Cart.objects.create(user=request.user, product=product, count=count)
        finally:
            cart.save()

        return redirect('main:product', pk=product_id)
    return redirect('user:login')

def checkout(request):
    return render(request, 'checkout.html')
