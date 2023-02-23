from django.shortcuts import render, redirect
from django.views import View
from userapp.models import *
from .models import *
from asosiy.models import *


class StatsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            tanlov = request.GET.get('ustun')
            soz = request.GET.get('soz')
            stats = Stats.objects.filter(ombor=o)
            if tanlov == 'm' and soz != "":
                m = Mahsulot.objects.filter(nom__contains=soz)|Mahsulot.objects.filter(brend__contains=soz)
                if m:
                    stats = Stats.objects.filter(mahsulot=m[0], ombor=o)
                    for i in m:
                        stats = stats | Stats.objects.filter(mahsulot=i, ombor=o)
            elif tanlov == 'c' and soz != "":
                c = Client.objects.filter(nom__contains=soz)|Client.objects.filter(dokon__contains=soz)
                if c:
                    stats = Stats.objects.filter(client=c[0], ombor=o)
                    for i in c:
                        stats = stats | Stats.objects.filter(client=i, ombor=o)
            data = {
                "statslar":stats,
                "mahsulotlar":Mahsulot.objects.filter(ombor=o),
                "clients":Client.objects.filter(ombor=o)
            }
            return render(request, 'stats.html', data)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Stats.objects.create(
                mahsulot=Mahsulot.objects.get(id=request.POST.get('m')),
                client=Client.objects.get(id=request.POST.get('c')),
                sana=request.POST.get('sana'),
                miqdor=request.POST.get('miqdor'),
                umumiy=request.POST.get('umumiy'),
                nasiya=request.POST.get('nasiya'),
                tolandi=request.POST.get('tolandi'),
                ombor=Ombor.objects.get(user=request.user)
                )
            return redirect('/stats/')
        return redirect('login')



class StatsEditView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            s = Stats.objects.get(id=pk)
            o = Ombor.objects.get(user=request.user)
            m = Mahsulot.objects.filter(ombor=o)
            c = Client.objects.filter(ombor=o)
            data = {
                "stats": s,
                'mahsulotlar':m,
                'clients':c
            }
            return render(request, 'stats_update.html',data)
        return redirect('login')


    def post(self, request, pk):
        if request.user.is_authenticated:
            if request.method == "POST":
                Stats.objects.filter(id=pk).update(
                    sana=request.POST['s'],
                    miqdor=request.POST['m'],
                    umumiy=request.POST['u'],
                    tolandi=request.POST['t'],
                    nasiya=request.POST['n'],
                )
                return redirect('/stats/')
        return redirect('login')