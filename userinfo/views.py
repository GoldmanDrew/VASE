from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


# Create your views here.



def agentDisplay(request):
    current_agent = Agent.objects.get(Agent=request.user)  # can now access all the agent, cash, wealth, and email fields of the specific user that is logged in
    current_agent_shares = AgentShare.objects.filter(Agent=current_agent)
    context = {"current_agent": current_agent , "current_agent_shares": current_agent_shares}
    return render(request, "userinfo/YourInfo.html", context )
