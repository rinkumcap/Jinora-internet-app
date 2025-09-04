'''
===============================================================================================================
                           AboutUs Form
===============================================================================================================
'''   
from django import forms
from app.models import *
class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['name', 'platform', 'tagline', 'logo_image', 'main_image','main_image1','main_image2','download_file','download_link','is_active']
        widgets = {
            'section_type': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'button_text': forms.TextInput(attrs={'class': 'form-control'}),
            'is_deleted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

