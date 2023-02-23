from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import *


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        u = User.objects.create_user(
            username=request.POST['l'],
            password=request.POST['p']
        )
        Ombor.objects.create(
            ism=request.POST['i'],
            dokon_nomi=request.POST['d'],
            tel=request.POST['t'],
            manzil=request.POST['m'],
            user=u

        )
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        u = request.POST.get('l')
        p = request.POST.get('p')
        users = authenticate(username=u, password=p)
        if users is None:
            return redirect('login')
        login(request, users)
        return redirect('bolim')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
