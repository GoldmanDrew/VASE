from django.contrib.auth.models import User
from django import forms
from landingpage.models import *

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']
