from django.shortcuts import render
from django.views import generic
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['Direction', 'OrderBookName', 'Type', 'Price', 'Quantity']


def getuser(request):
    current_agent = Agent.objects.get(Agent=request.user)
    return current_agent

def orderpage(request):
    all_orders = orderfilter(request)
    all_companies = Company.objects.all()
    all_asks = all_orders.filter(Direction="A")
    all_bids = all_orders.filter(Direction="B")
    all_orders = Order.objects.filter(Agent=getuser(request))

    form = OrderForm(request.POST or None)
    if form.is_valid():
        new_order = form.save(commit = False)
        new_order.Agent = getuser(request)
        new_order.QuantityToFill = new_order.Quantity
        if new_order.Type == "M" and new_order.Direction == "A":
            new_order.Price = 0
        if new_order.Type == "M" and new_order.Direction == "B":
            new_order.Price = 2147483647
        new_order.save()
        form = OrderForm()

    context = {
        "all_asks" : all_asks,
        "all_bids" : all_bids,
        "all_orders" : all_orders,
        "all_companies" : all_companies,
        "form": form
    }
    return render(request, "order/orderpage.html", context)

def orderfilter(request):
    all_orders = Order.objects.all()
    all_companies = Company.objects.all()
    companies = request.GET.get('company_form')
    if companies != "" and companies!= None:
        all_orders = all_orders.filter(OrderBookName=companies)
    return all_orders
