from django.shortcuts import render, redirect
from django.views import generic
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # self.fields['Type'].help_text = "" # replaced by tooltip
        self.fields['Price'].required = False

    class Meta:
        model = Order
        fields = ['Direction', 'OrderBookName', 'Type', 'Price', 'Quantity']
        labels = {
            'OrderBookName': 'Class',
        }

    def clean(self):
        order_type = self.cleaned_data.get('Type', None)
        if order_type == "L":
            # validate that price is empty
            price = self.cleaned_data.get('Price', None)
            if price == None:
                self._errors['Price'] = self.error_class([
                    'Price is required'])
        return super().clean()

def goToOrder(request, className):
    form_class = OrderForm
    form = form_class(initial={'OrderBookName': className})
    context = {
        'form': form,
    }
    return render(request, 'order/orderpage.html', context)

def getuser(request):
    current_agent = Agent.objects.get(Agent=request.user)
    return current_agent


def orderpage(request):
    current_agent = Agent.objects.get(Agent=request.user)
    all_orders = orderfilter(request)
    all_orders = Order.objects.filter(Agent=getuser(request), Filled="N")
    all_companies = Company.objects.all()
    all_asks = all_orders.filter(Direction="A")
    all_bids = all_orders.filter(Direction="B")

    form = OrderForm(request.POST or None)

    context = {
        "all_asks": all_asks,
        "all_bids": all_bids,
        "all_orders": all_orders,
        "all_companies": all_companies,
        "current_agent": current_agent,
        "form": form,
    }
    return render(request, "order/orderpage.html", context)


def postorder(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.Agent = getuser(request)
            new_order.QuantityToFill = new_order.Quantity
            if new_order.Type == "M" and new_order.Direction == "A":
                new_order.Price = 0
            if new_order.Type == "M" and new_order.Direction == "B":
                new_order.Price = 2147483647
            instance = new_order.save()
            # serialize in new object in json
            # ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            form = OrderForm()
            return JsonResponse({"instance": "success"}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    # some other error occurred
    messages.error(request, "Error submitting order.")
    return JsonResponse({"error": ""}, status=400)


def cancelorder(request, pk):
    print("at least this is working")
    if request.is_ajax: # and request.method == "POST":
        order = Order.objects.get(pk=pk)
        order.Filled = "C"
        instance = order.save(update_fields=["Filled"])
        return JsonResponse({"canceled": pk}, status=200)
    return JsonResponse({"error": ""}, status=400)


def yourorders(request):
    current_agent = Agent.objects.get(Agent=request.user)
    all_orders = orderfilter(request)
    all_orders = Order.objects.filter(Agent=getuser(request), Filled="N")
    all_companies = Company.objects.all()
    all_asks = all_orders.filter(Direction="A")
    all_bids = all_orders.filter(Direction="B")
    context = {
        "all_orders": all_orders,
        "all_companies": all_companies,
        "current_agent": current_agent,
    }
    return render(request, "order/yourorders.html", context)


def allorders(request):
    current_agent = Agent.objects.get(Agent=request.user)
    all_orders = orderfilter(request)
    all_orders = Order.objects.filter(Agent=getuser(request), Filled="N")
    all_companies = Company.objects.all()
    all_asks = all_orders.filter(Direction="A")
    all_bids = all_orders.filter(Direction="B")
    context = {
        "all_asks": all_asks,
        "all_bids": all_bids,
        "all_companies": all_companies,
        "current_agent": current_agent,
    }
    return render(request, "order/allorders.html", context)


def orderfilter(request):
    all_orders = Order.objects.all()
    all_companies = Company.objects.all()
    companies = request.GET.get('company_form')
    if companies != "" and companies != None:
        all_orders = all_orders.filter(OrderBookName=companies)
    return all_orders
