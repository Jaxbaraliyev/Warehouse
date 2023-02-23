from django.shortcuts import render, redirect
from django.views import View
from statsapp.models import *
from .models import *
from userapp.models import *


class BolimView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        return redirect('login')


class MahsulotView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            data = {
                'mahsulotlar': Mahsulot.objects.filter(ombor=o)
            }
            return render(request, 'products.html', data)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Mahsulot.objects.create(
                    nom=request.POST.get('pr_name'),
                    brend=request.POST.get('pr_brand'),
                    kelgan_narx=request.POST.get('pr_kelgan'),
                    sotuv_narx=request.POST.get('pr_sotuv'),
                    miqdor=request.POST.get('pr_miqdor'),
                    ombor=Ombor.objects.get(user=request.user)
                )
                return redirect('mahsulotlar')
        return redirect('login')


class MahsulotEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            m = Mahsulot.objects.get(id=pk)
            return render(request, 'product_update.html', {'product':m})
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Mahsulot.objects.filter(id=pk).update(
                    miqdor=request.POST['d'],
                    kelgan_narx=request.POST['k_n'],
                    sotuv_narx=request.POST['s_n']
                )
                return redirect('mahsulotlar')
        return redirect('login')





class ClientView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            data = {
                "clients":Client.objects.filter(ombor=o)
            }
            return render(request, 'clients.html', data)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Client.objects.create(
                    nom=request.POST['n'],
                    dokon=request.POST['d'],
                    tel=request.POST['t'],
                    manzil=request.POST['m'],
                    qarz=request.POST['q'],
                    ombor=Ombor.objects.get(user=request.user),
            )
            return redirect('clients')
        return redirect('login')


class ClientEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            c = Client.objects.get(id=pk)
            return render(request, 'client_update.html',{"client":c})
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            if request.method == 'POST':
                Client.objects.filter(id=pk).update(
                    nom=request.POST['n'],
                    dokon=request.POST['d'],
                    tel=request.POST['t'],
                    qarz=request.POST['q'],
                    manzil=request.POST['m'],
                )
                return redirect('clients')
        return redirect('login')