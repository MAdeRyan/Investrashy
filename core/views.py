from django.shortcuts import render, redirect
from core.forms import UserForm,UserProfileInfoForm,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'invest/index.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    context = {
        'page':'Daftar',
    }
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user                      
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True            
        else:
            print(user_form.errors,profile_form.errors)
            context['error'] = 'username sudah digunakan'
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()        
    
    context['user_form'] = user_form
    context['profile_form'] = profile_form
    context['registered'] = registered               
    return render(request,'core/registration.html', context)
    
def user_login(request):
    login_form = LoginForm()
    context = {'page': 'Masuk','login_form':login_form,}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                context['error'] = 'Your Account was Unactive'
                return render(request, 'core/login.html', context)
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            context['error'] = "Username/Password Incorrect"
            return render(request, 'core/login.html', context)        
    else:        
        return render(request, 'core/login.html', context)
