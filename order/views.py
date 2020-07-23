from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import Company, Agent, AgentShare, Order, Price
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['Direction', 'OrderBookName', 'Type', 'Price', 'Quantity']

def orderpage(request):
    all_orders = orderfilter(request)
    all_companies = Company.objects.all()
    all_asks = all_orders.filter(Direction="A")
    all_bids = all_orders.filter(Direction="B")
    all_orders = Order.objects.filter(Agent="alan")

    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
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
    all_orders = Order.objects.filter(Agent="alan")
    all_companies = Company.objects.all()
    companies = request.GET.get('company_form')
    if companies != "" and companies!= None:
        all_orders = all_orders.filter(OrderBookName=companies)
    return all_orders
