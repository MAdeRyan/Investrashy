from django import forms
from core.models import UserProfileInfo
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')

class UserForm(forms.ModelForm):    
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email','first_name')
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Nama Lengkap:'
        self.fields['email'].label = 'Email:'
    
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
         model = UserProfileInfo
         fields = ('no_telp','profile_pic')

         widgets = {        
            'profile_pic': forms.FileInput(
                attrs={
                    'id': 'upload-photo', 
                    'onchange': 'loadFile(event)',
                }
            ),                
         }
    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].label = ''