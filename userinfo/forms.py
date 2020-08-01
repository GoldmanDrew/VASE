from django.contrib.auth.models import User
from django import forms
from landingpage.models import *

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateUserForm2(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=100, required=False)
    old_password = forms.CharField(widget=forms.PasswordInput, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    verify_password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'old_password', 'password', 'verify_password']


class UpdateUserForm3(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdatePass(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    verify_password = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'verify_password']
