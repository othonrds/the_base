from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
<<<<<<< HEAD
    path('create-product/', views.create_product, name="create-product"),
=======

    path('create-plan/', views.create_plan, name="create-plan"),
    
>>>>>>> 76ef6bd1a50387b6846e6d4fe1a14682d20e8a78
]