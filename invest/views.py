from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import UserProfileInfo
from invest.models import InvestasiModel
from invest.forms import InvestasiForm
from core.forms import UserForm,UserProfileInfoForm,LoginForm
from django.db.models import Q


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
    
    if request.GET:        
        query = request.GET['search']
        data = InvestasiModel.objects.filter(Q(jenis_sampah__icontains=query)|Q(alamat__icontains=query))
    else:                
        data = InvestasiModel.objects.all()
    context['data'] = data
    return render(request, 'invest/beranda.html', context)

@login_required
def reward(request):
    context = {
        'page': 'Investasi Sampah | Reward',        
        }
    data = InvestasiModel.objects.filter(user=request.user)
    context['data'] = data
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
            model = invest_form.save(commit=False)                                          
            model.user = request.user
            model.save()                    
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
    data = InvestasiModel.objects.filter(user=request.user)
    context['data'] = data
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
    if not request.user.is_superuser:
        dataUser = User.objects.get(pk=request.user.id)
        advancedData = UserProfileInfo.objects.get(user=request.user)
        context['dataUser'] = dataUser
        context['advancedData'] = advancedData
        return render(request, 'invest/profile.html', context)  
    return render(request, 'invest/profile.html', context)  