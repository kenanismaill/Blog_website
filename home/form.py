from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='User Name :')
    first_name = forms.CharField(max_length=50, label='First Name :')
    last_name = forms.CharField(max_length=50, label='Last Name :')
    email = forms.CharField(max_length=100, label='Email :')

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
