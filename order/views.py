from django.shortcuts import render
from django.http import HttpResponse
from order.models import Company # have to import each of our models (here, we are importing the Company class from models.py)
from django.contrib import messages

# Create your views here. FOR THE ORDER APP (b/c this is the views.py file within the order app)
def index(request):
    return render(request, 'order/index.html')

def summary(request):
    return render(request, 'order/summary.html')
