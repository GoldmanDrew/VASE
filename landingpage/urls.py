# urls that are relevant to the order page
from django.urls import path
from . import views

app_name = "landingpage"

urlpatterns = [
    path('', views.LandingPage, name='form-index'),
    path('register/', views.RegisterView.as_view(), name='register_url'),
    path('login/', views.login_request, name='login_url'),
    path('logout/', views.logout_request, name="logout_url"),
]
