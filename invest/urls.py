from django.urls import path

from . import views

app_name = 'invest'
urlpatterns = [
    path('', views.index, name='index'),
    path('beranda/', views.beranda, name='beranda'),
    path('beranda/detail', views.detail, name='detail'),
    path('investasi/', views.investasi, name='investasi'),
    path('investasi/tambah', views.tambah, name='tambah'),
    path('investasi/riwayat', views.riwayat, name='riwayat'),
    path('reward/', views.reward, name='reward'),
    path('histori/', views.histori, name='histori'),
    path('messages/', views.chat, name='chat'),
    path('messages/id', views.messages, name='messages'),
]