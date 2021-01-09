from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
<<<<<<< HEAD
        exclude = ['user']       

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'         
=======
        exclude = ['user']   

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        exclude = ['customer']            
>>>>>>> 76ef6bd1a50387b6846e6d4fe1a14682d20e8a78
