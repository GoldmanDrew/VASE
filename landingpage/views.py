from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.urls import reverse_lazy
from order.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm     # imports the format for Login/Register



# Create your views here. FOR THE ORDER APP (b/c this is the views.py file within the order app)


class UserFormView(View):
    form_class = UserForm
    template_name = 'landingpage/registration_form.html'    # need to create this file

    # displays blank form (new person registering)
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)    # request.POST saves the user-inputted fields

        if form.is_valid():
            user = form.save(commit=False)  # doesn't save to database yet (stores locally)

            # formatted data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            a = Agent(Agent=username, Cash=1000, Wealth=0, Email=email)
            a.save()

            # still need to create new Agent

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('order/')     # need to find another page to redirect to

        return render(request, self.template_name, {'form': form})


# Create your views here.
