from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/', views.profile, name="profile"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),

    path('create-plan/', views.create_plan, name="create-plan"),
    
]