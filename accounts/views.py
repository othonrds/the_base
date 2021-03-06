from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import  CustomerForm , PlanForm
from .decorators import unauthenticated_user, authenticated_user #, allowed_users

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

@authenticated_user
def profile(request):
    customer = request.user.customer
    plans = customer.plan_set.all()
    plans_total = plans.count()
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form' : form, 'plans' : plans,'plans_total' : plans_total }
    return render(request, 'accounts/profile.html', context)
    
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # adicionando ao group customer (LOGICA NO SIGNALS)
            #            
            # group = Group.objects.get(name='customer')
            # instance.user.groups.add(group)
            #
            # Customer.objects.create(
            #     user=user,
            #     name=user.username,
            #     )

            # Criando um model Customer associado ao usuário
            

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
    context = {'form':form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username Or password is incorrect')
            
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

#@allowed_users(allowed_roles=['admin', 'staff'...]
<<<<<<< HEAD
#def dashboardPage(request):    

def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
=======
#def dashboardPage(request):  


#@login_required(login_url='login')
   
def create_plan(request):
    customer = request.user.customer
    form = PlanForm()
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=customer)
>>>>>>> 76ef6bd1a50387b6846e6d4fe1a14682d20e8a78
        if form.is_valid():
            form.save()
            return redirect('/')

<<<<<<< HEAD
    context = {'form':form}
    return render(request, 'accounts/product_form.html', context)
=======
    context = {'form':form }
    return render(request, 'accounts/plan_form.html', context)

 
>>>>>>> 76ef6bd1a50387b6846e6d4fe1a14682d20e8a78
