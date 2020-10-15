# urls that are relevant to the order page
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "landingpage"

urlpatterns = [
    path('', views.login_request, name='login_url'),
    path('about-us/', views.about, name='about_url'),
    path('register/', views.RegisterView.as_view(), name='register_url'),
    path('login/', views.login_request, name='login_url'),
    path('logout/', views.logout_request, name="logout_url"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
