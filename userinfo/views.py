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
    current_agent = Agent.objects.get(Agent=request.user)
    current_agent_shares = AgentShare.objects.filter(Agent=current_agent)

    if request.method == "POST":
        form_user = UpdateUserForm(request.POST, instance=request.user)
        form_pass = PassChangeForm(user=request.user, data=request.POST)
        if form_pass.has_changed():
            if form_pass.is_valid() and form_user.is_valid():
                form_pass.save()
                update_session_auth_hash(request, form_pass.user)

                user = form_user.save(commit=False)
                if form_user.cleaned_data['username'] != "":
                    current_agent.Agent = form_user.cleaned_data['username']
                    current_agent.save()
                else:
                    user.username = current_agent.Agent

                if form_user.cleaned_data['email'] != "":
                    current_agent.Email = form_user.cleaned_data['email']
                    current_agent.save()
                else:
                    user.email = current_agent.Email

                user.save()
                return redirect('/userinfo/')
        elif form_user.is_valid():
            user = form_user.save(commit=False)
            if form_user.cleaned_data['username'] != "":
                current_agent.Agent = form_user.cleaned_data['username']
                current_agent.save()
            else:
                user.username = current_agent.Agent

            if form_user.cleaned_data['email'] != "":
                current_agent.Email = form_user.cleaned_data['email']
                current_agent.save()
            else:
                user.email = current_agent.Email

            user.save()
            return redirect('/userinfo/')

    else:
        form_user = UpdateUserForm(instance=request.user)
        form_pass = PassChangeForm(user=request.user)

    context = {
        "current_agent": current_agent,
        "current_agent_shares": current_agent_shares,
        "form_user": form_user,
        "form_pass": form_pass
    }
    return render(request, "userinfo/yourinfo.html", context )
