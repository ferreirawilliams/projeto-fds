from pickle import TRUE
from pyexpat import model
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
  class Meta:
    model = User
    fields = [
      'username',
      'email',
      'password',
    ]
    labels ={
      'username':'Nome de Usuario',
      'email':'Digite o seu email',
      'password': 'Digite a sua senha'
    }
    help_texts = {
      'email':'The e-mail must be valid.'
    }

    widgets = {
      'username': forms.TextInput(attrs={
        'placeholder':'type your name here'
      }),
      'email': forms.EmailInput(attrs={
        'placeholder':'type your email here',
      }),
      'password': forms.PasswordInput(attrs={
        'placeholder':'type your password here',
      })
    }
    
