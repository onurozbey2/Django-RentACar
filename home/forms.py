from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Kullanıcı Adı')
    email = forms.EmailField(max_length=100, label='E-mail')
    first_name = forms.CharField(max_length=40, help_text='Ad', label='Ad')
    last_name = forms.CharField(
        max_length=40, help_text='Soyad', label='Soyad')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
