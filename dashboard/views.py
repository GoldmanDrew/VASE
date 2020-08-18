from django.shortcuts import render, redirect
from django.views import generic
from dashboard.models import *
import json
from django.http import HttpResponse
from django.core import serializers

def classview(request):
    all_tokens = Token.objects.all()
    all_tokens_json = serializers.serialize('json', all_tokens)
    context = {
        "all_tokens" : all_tokens,
        "all_tokens_json" : all_tokens_json,
    }
    return render(request, "dashboard/dashboard.html", context)

def priceview(request):
    if request.method == 'GET':
        class_name = request.GET['class']
        print(class_name)
        all_prices = Token.objects.filter(Name = class_name);
        context = {
            "all_prices" : all_prices
        }
        json_data = serializers.serialize('json', all_prices)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse("unsuccesful")
