from django.shortcuts import render, redirect
from django.views import generic
from order.models import *
import json
from django.http import HttpResponse
from django.core import serializers

def classview(request):
    all_companies = Company.objects.all()
    all_prices = Price.objects.all()
    all_prices_json = serializers.serialize('json', all_prices)
    context = {
        "all_classes" : all_companies,
        "all_prices" : all_prices,
        "all_prices_json" : all_prices_json,
    }
    return render(request, "class/classpage.html", context)

def priceview(request):
    if request.method == 'GET':
        class_name = request.GET['class']
        class_ticker = Company.objects.get(ClassName = class_name)
        all_prices = Price.objects.filter(OrderBookName = class_ticker)
        context = {
            "all_prices" : all_prices
        }
        json_data = serializers.serialize('json', all_prices)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse("unsuccesful")
