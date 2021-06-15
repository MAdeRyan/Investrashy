from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class InvestasiModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="", null=True)    
    cSampah = (
        ('Plastik', 'plastik'),
        ('Organik', 'organik'),
        ('Lainnya', 'lainnya'),
    )

    jenis_sampah = models.CharField(max_length=50, choices=cSampah)
    alamat = models.CharField(max_length=50)
    deskripsi = models.TextField(max_length=140)
    gambar = models.ImageField(blank=True, upload_to='investasi_pics/')   