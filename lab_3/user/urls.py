from django.urls import re_path

from . import views

app_name = "user"
urlpatterns = [
    re_path(r'^profile/?$', views.profile, name='profile'),
    re_path(r'^logout/?$', views.logout, name='logout'),
    re_path(r'^password_change/?$', views.password_change, name='password_change'),
    re_path(r'^login/?$', views.login, name='login'),
    re_path(r'^signup/?$', views.signup, name='signup'),
]