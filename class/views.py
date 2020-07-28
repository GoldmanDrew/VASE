from django.shortcuts import render, redirect
from django.views import generic
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from order.models import *


def classview(request):
    all_companies = Company.objects.all()
    depart_colors = {"Mathematics":"bg-primary", "Computer Science":"bg-light", "Applied Mathematics": "bg-dark"}
    context = {
        "all_classes" : all_companies,
        "depart_colors" : depart_colors,
        "Mathematics":"bg-primary",
    }
    return render(request, "class/classpage.html", context)
