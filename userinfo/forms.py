from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from landingpage.models import *

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

class PassChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].required=False
        self.fields['new_password1'].required=False
        self.fields['new_password2'].required=False
