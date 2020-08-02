from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.urls import reverse_lazy
from order.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token_generator import account_activation_token
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm     # imports the format for Login/Register


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
                messages.success(request, f"You are now logged in as {username}")
                return redirect('userinfo:userinfo-display')  # need to find another page to redirect to
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    # return render(request, "landingpage/index.html", {'form': form})
    return render(request, "landingpage/login_form.html", {'form': form})


def logout_request(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("landingpage:login_url")


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

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            verify_password = form.cleaned_data['verify_password']

            if password != verify_password:
                messages.error(request, "Your passwords do not match")
            if email[email.find('@'):] != '@virginia.edu':
                messages.error(request, "Please enter a valid UVA email address")
            if password == verify_password and email[email.find('@'):] == '@virginia.edu':
                user = form.save(commit=False)  # doesn't save to database yet (stores locally)

                user.is_active = False
                user.set_password(password)
                user.save()

                a = Agent(Agent=username, Cash=1000, Wealth=0, Email=email)
                a.save()

                for company in Company.objects.all():
                    b = AgentShare(Agent=a, Company=company, Shares=50, Borrowed=0, Collateral=0)
                    b.save()

                current_site = get_current_site(request)
                mail_subject = 'Activate your VASE account.'
                message = render_to_string('landingpage/activate_account.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data['email']
                email_final = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email_final.send()
                return render(request, 'landingpage/email_conf.html', {'email': email})

        return render(request, self.template_name, {'form': form})

    '''
            if password != verify_password:
                messages.error(request, "Your passwords do not match")
            else:

                user.set_password(password)
                user.save()

                a = Agent(Agent=username, Cash=1000, Wealth=0, Email=email)
                a.save()

                for company in Company.objects.all():
                    b = AgentShare(Agent=a, Company=company, Shares=50, Borrowed=0, Collateral=0)
                    b.save()

                user = authenticate(username=username, password=password)

                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('landingpage:login_url')     # need to find another page to redirect to

            return render(request, self.template_name, {'form': form})
    '''


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        # uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user)
        messages.success(request, 'Thank you for your email confirmation. Now you can login into your account.')
        return redirect('landingpage:login_url')  # need to find another page to redirect to
    else:
        messages.error(request, 'Your activation link is invalid')
        return redirect('landingpage:login_url')

# Create your views here.
