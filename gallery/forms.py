from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import EmailInput, TextInput


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control', 'required': True}),
            'email': EmailInput(attrs={'type':'email', 'class':'form-control', 'required':True}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



