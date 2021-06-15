from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import UserProfileInfo
from invest.models import InvestasiModel
from invest.forms import InvestasiForm
from core.forms import UserForm,UserProfileInfoForm,LoginForm

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
    data = InvestasiModel.objects.all()
    context['data'] = data
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
def detail(request, invest_id):
    context = {
        'page': 'Investasi Sampah | Detail',        
        }    
    data = InvestasiModel.objects.get(pk=invest_id)
    context['data'] = data
    return render(request, 'invest/detail.html', context)
@login_required
def tambah(request):
    context = {
        'page': 'Investasi Sampah | Tambah Investasi',        
        }
    if request.method == 'POST':
        invest_form = InvestasiForm(request.POST, request.FILES)        
        if invest_form.is_valid():             
            invest_form.user = request.user
            invest_form.save()            
        return redirect('invest:beranda')
    else:        
        invest_form = InvestasiForm()
        context['invest_form'] = invest_form             
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
    if request.user.username != 'admin':
        dataUser = User.objects.get(pk=request.user.id)
        advancedData = UserProfileInfo.objects.get(user=request.user)
        context['dataUser'] = dataUser
        context['advancedData'] = advancedData
        return render(request, 'invest/profile.html', context)  
    return render(request, 'invest/profile.html', context)  