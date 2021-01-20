from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('login', views.Login.as_view(), name = 'login'),
    path('logout',views.Logout.as_view(), name = 'logout'),
    path('signup', views.UserCreate.as_view(), name = 'signup'),
    path('home', views.home, name = 'home'),
]