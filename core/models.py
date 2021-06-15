# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    no_telp = models.IntegerField(_('No Telepon'))    
    profile_pic = models.ImageField(_('Foto Profil'),upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username