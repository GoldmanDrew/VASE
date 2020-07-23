from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.urls import reverse_lazy
from order.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, LoginForm     # imports the format for Login/Register


# Create your views here. FOR THE ORDER APP (b/c this is the views.py file within the order app)


def LandingPage(request):
    return render(request, 'landingpage/index.html')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('order:order-index')  # need to find another page to redirect to
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, "landingpage/login_form.html", {'form': form})
    # return render(request, 'landingpage/loginpage.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("landingpage:login_url")


'''
class LoginView(View):
    
    form_class = AuthenticationForm
    template_name = 'landingpage/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)    # request.POST saves the user-inputted fields

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('order:order-index')  # need to find another page to redirect to
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

        return render(request, self.template_name, {'form': form})
'''


class RegisterView(View):
    form_class = RegistrationForm
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


            # for company in Company.objects.all():
                # b = AgentShare(Agent=a, Company=company, Shares=50, Borrowed=0, Collateral=0)
                # b.save()
                # print(company)

            # still need to create new Agent

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('landingpage:login_url')     # need to find another page to redirect to

        return render(request, self.template_name, {'form': form})


# Create your views here.
