from django.shortcuts import render, redirect, get_list_or_404
from django.views import generic
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView)
from .forms import LoginForm, UserCreateForm
from .models import User
import requests

# Create your views here.
class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'

class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'homepage.html'
    # model = ProfileModel

class UserCreate(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('create_profile')
    template_name = 'signup.html'

    def form_valid(self,form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username = username, password = password)
        login(self.request,user)
        return response

class UserDelete(LoginRequiredMixin, generic.View):
    def get(self, *args, **kwargs):
        user = User.objects.get(username = self.request.user.username)
        user.is_active = False
        user.save()
        logout(self.request)
        return render(self.request,'user_delete.html')