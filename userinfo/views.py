from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .forms import UpdateUserForm, UpdateUserForm, PassChangeForm
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def agentDisplay(request):
    current_user = request.user
    current_username = request.user.username
    current_email = request.user.email
    current_user_shares = UserShare.objects.filter(User=current_email)

    if request.method == "POST":
        form_user = UpdateUserForm(request.POST, instance=request.user)
        form_pass = PassChangeForm(user=request.user, data=request.POST)
        if form_pass.has_changed():
            if form_pass.is_valid() and form_user.is_valid():
                form_pass.save()
                update_session_auth_hash(request, form_pass.user)

                user = form_user.save(commit=False)
                if form_user.cleaned_data['username'] == "":
                    user.username = current_username

                email = form_user.cleaned_data['email']
                if email != "":
                    if email[email.find('@'):] != '@virginia.edu':
                        messages.error(request, "Please enter a valid UVA email address")
                    else:
                        for user_shares in current_user_shares:
                            user_shares.User = form_user.cleaned_data['email']
                            user_shares.save()
                else:
                    user.email = current_email

                user.save()
                return redirect('/userinfo/')
        elif form_user.is_valid():
            user = form_user.save(commit=False)
            if form_user.cleaned_data['username'] == "":
                user.username = current_username

            email = form_user.cleaned_data['email']
            if email != "":
                if email[email.find('@'):] != '@virginia.edu':
                    messages.error(request, "Please enter a valid UVA email address")
                else:
                    for user_shares in current_user_shares:
                        user_shares.User = form_user.cleaned_data['email']
                        user_shares.save()
            else:
                user.email = current_email

            user.save()
            return redirect('/userinfo/')

    else:
        form_user = UpdateUserForm(instance=request.user)
        form_pass = PassChangeForm(user=request.user)

    context = {
        "current_user": current_user,
        "current_user_shares": current_user_shares,
        "form_user": form_user,
        "form_pass": form_pass
    }
    return render(request, "userinfo/yourinfo.html", context)
