from django import forms
from invest.models import InvestasiModel

class InvestasiForm(forms.ModelForm):
    class Meta():
        model = InvestasiModel
        fields = ('gambar', 'jenis_sampah', 'alamat', 'deskripsi')

        widgets = {        
            'gambar': forms.FileInput(
                attrs={
                    'id': 'upload-photo',                    
                }
            ),   
            'jenis_sampah': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),   
            'alamat': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan alamat',
                }
            ),  
            'deskripsi': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tuliskan deskripsi',
                }
            ),                              
        }
    def __init__(self, *args, **kwargs):
        super(InvestasiForm, self).__init__(*args, **kwargs)
        self.fields['gambar'].label = ''        