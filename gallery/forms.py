from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import EmailInput, PasswordInput, TextInput, FileInput, Select, Textarea
from .models import Photo


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control', 'required': True}),
            'email': EmailInput(attrs={'type':'email', 'class':'form-control', 'required':True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class LoginUserForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}), max_length=100)
    password = forms.CharField(widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'image_name', 'image_description',
                  'location', 'category')
        labels = {
            'image': 'Select Image',
            'image_name': 'Name',
            'image_description': 'Description'
        }
        widgets = {
            'image': FileInput(attrs={'class': 'form-control mt-1'}),
            'location': Select(attrs={'class': 'form-select mt-1'}),
            'category': Select(attrs={'class': 'form-select mt-1'}),
            'image_name': TextInput(attrs={'class': 'form-control mt-1'}),
            'image_description': Textarea(attrs={'class': 'form-control mt-1'}),
        }
