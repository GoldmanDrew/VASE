from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import Company, Agent, AgentShare, Order, Price
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


# Create your views here.


def agentDisplay(request):
    agentTable = Agent.objects.all()
    agentShares = AgentShare.objects.all()
    context = {'agentTable': agentTable, 'agentShares': agentShares}
    return render(request, "userinfo/YourInfo.html", context)

'''
def sharesDisplay(request):
    agentShares = AgentShare.objects.all()
    return render(request, "userinfo/YourInfo.html", {'agentShares' : agentShares })
'''
