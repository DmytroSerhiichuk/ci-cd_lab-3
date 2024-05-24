from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = MyUser
        fields = ('first_name', 'second_name', 'email', 'password1', 'password2')

class SignupForm(AuthenticationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = MyUser
        fields = ('email', 'password1')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('first_name', 'second_name', 'email')