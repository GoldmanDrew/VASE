from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. FOR THE ORDER APP (b/c this is the views.py file within the order app)
def index(request):
    return render(request, 'order/index.html')

def summary(request):
    return render(request, 'order/summary.html')
