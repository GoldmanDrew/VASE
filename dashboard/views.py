from django.shortcuts import render, redirect
from django.views import generic
from dashboard.models import *
import json
from django.http import HttpResponse
from django.core import serializers

def classview(request):
    all_tokens = Token.objects.all()

    all_token_history = TokenHistory.objects.all()
    all_tokens_history_json = serializers.serialize('json', all_token_history)

    context = {
        "all_tokens" : all_tokens,
        "all_tokens_history_json" : all_tokens_history_json,
    }
    return render(request, "dashboard/dashboard.html", context)

def priceview(request):
    if request.method == 'GET':
        class_name = request.GET['class']
        curr_token = Token.objects.get(Name = class_name)
        all_prices = TokenHistory.objects.filter(Token = curr_token);
        context = {
            "all_prices" : all_prices
        }
        json_data = serializers.serialize('json', all_prices)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse("unsuccesful")
