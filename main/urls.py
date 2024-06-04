from django.urls import path, re_path

from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^shop/?$', views.shop, name='shop'),
    re_path(r'^shop/(?P<category_link>.+)/?$', views.category, name='category'),
    re_path(r'^product/(?P<pk>\d+)/?$', views.product, name='product'),
]