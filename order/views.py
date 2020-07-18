from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.urls import reverse_lazy
from .models import Company, Agent, AgentShare, Order, Price
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


# Create your views here. FOR THE ORDER APP (b/c this is the views.py file within the order app)

class OrderCreate(CreateView):
    model = Order
    fields = ['Direction', 'OrderBookName', 'Type', 'Price', 'Quantity']

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.helper = FormHelper()
    #    self.helper.layout = Layout(
    #        Fieldset(
    #            HTML("""
    #                <p>We use notes to get better, <strong>please help us {{ username }}</strong></p>
    #            """),
    #
    #        )
    #    )
