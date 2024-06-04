from django.urls import path, re_path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='home'),
    path('cart/', views.cart, name='cart'),
    re_path(r'^shop/?$', views.shop, name='furnitureshop'),
    re_path(r'^shop/(?P<category_link>\w+)/?$', views.category, name='category'),
]