from django.shortcuts import render, redirect
from django.views import generic
from order.models import *
import json
from django.http import HttpResponse
from django.core import serializers

def classview(request):
    all_tokens = Token.objects.all()
    all_orders = Order.objects.all()
    all_orders_json = serializers.serialize('json', all_orders)
    context = {
        "all_classes" : all_tokens,
        "all_orders" : all_orders,
        "all_orders_json" : all_orders_json,
    }
    return render(request, "dashboard/dashboard.html", context)

def priceview(request):
    if request.method == 'GET':
        class_name = request.GET['class']
        all_orders = Order.objects.all();
        #all_orders = Price.objects.filter(OrderBookName = class_name)
        context = {
            "all_orders" : all_orders
        }
        print(class_ticker, prices, all_orders)
        json_data = serializers.serialize('json', all_orders)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse("unsuccesful")
