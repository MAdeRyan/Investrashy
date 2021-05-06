from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'invest/index.html')

def beranda(request):
    return render(request, 'invest/beranda.html')

def reward(request):
    return render(request, 'invest/reward.html')

def histori(request):
    return render(request, 'invest/histori.html')

def investasi(request):
    return render(request, 'invest/investasi.html')

def detail(request):
    return render(request, 'invest/detail.html')

def tambah(request):
    return render(request, 'invest/tambah-investasi.html')

def riwayat(request):
    return render(request, 'invest/riwayat.html')

def chat(request):
    return render(request, 'invest/user-messages.html')

def messages(request):
    return render(request, 'invest/messages.html')