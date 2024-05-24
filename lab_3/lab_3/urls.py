"""
URL configuration for lab_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    re_path(r'^profile/?$', views.profile, name='profile'),
    re_path(r'^password_change/?$', views.password_change, name='password_change'),
    re_path(r'^login/?$', views.login, name='login'),
    re_path(r'^signup/?$', views.signup, name='signup'),
    re_path(r'^shop/?$', views.shop, name='shop'),
    re_path(r'^shop/(?P<category_link>\w+)/?$', views.category, name='category'),
    # re_path(r'^(?P<product_link>.+)/?$', views.product, name='product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
