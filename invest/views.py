from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import UserProfileInfo

@login_required
def index(request):
    context = {
        'page': 'Investasi Sampah | Home',        
        }    
    return render(request, 'invest/index.html', context)
@login_required
def beranda(request):
    context = {
        'page': 'Investasi Sampah | Beranda',        
    }
    return render(request, 'invest/beranda.html', context)
@login_required
def reward(request):
    context = {
        'page': 'Investasi Sampah | Reward',        
        }
    return render(request, 'invest/reward.html', context)
@login_required
def histori(request):
    context = {
        'page': 'Investasi Sampah | Histori',        
        }
    return render(request, 'invest/histori.html', context)
@login_required
def investasi(request):
    context = {
        'page': 'Investasi Sampah | Investasi',        
        }
    return render(request, 'invest/investasi.html', context)
@login_required
def detail(request):
    context = {
        'page': 'Investasi Sampah | Detail',        
        }
    return render(request, 'invest/detail.html', context)
@login_required
def tambah(request):
    context = {
        'page': 'Investasi Sampah | Tambah Investasi',        
        }
    return render(request, 'invest/tambah-investasi.html', context)
@login_required
def riwayat(request):
    context = {
        'page': 'Investasi Sampah | Riwayat',        
        }
    return render(request, 'invest/riwayat.html', context)
@login_required
def chat(request):
    context = {
        'page': 'Investasi Sampah | Chat',        
        }
    return render(request, 'invest/user-messages.html', context)
@login_required
def messages(request):
    context = {
        'page': 'Investasi Sampah | Pesan',        
        }
    return render(request, 'invest/messages.html', context)
@login_required
def profile(request):
    context = {
        'page': 'Investasi Sampah | Profile',        
        }
    context['user_info'] = UserProfileInfo
    context['user_profile'] = User
    return render(request, 'invest/profile.html', context)
@login_required
def edit_profile(request):
    return render(request, 'invest/edit_profile.html')