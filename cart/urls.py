from django.urls import path, re_path

from . import views

app_name = "cart"
urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^add/?$', views.add, name='add'),
    re_path(r'^checkout/?$', views.checkout, name='checkout'),
]