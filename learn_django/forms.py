from django import forms
from learn_django.models import Product, CustomUser
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

class productform (forms.ModelForm):
    class Meta:
        model= Product
        fields = ('name', 'price','description')

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')