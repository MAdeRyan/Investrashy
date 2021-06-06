from django.db import models
from django.conf import settings

# Create your models here.

class Investasi(models.Model):
    jenis_sampah = models.CharField(max_length=50)
    alamat = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=140)
    gambar = models.ImageField(blank=True)