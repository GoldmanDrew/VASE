"""market_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path( '' , )  Whenever you leave the first parameter as '', that is the page that will be loaded
    # when the user goes to http://127.0.0.1:8000/ or http://127.0.0.1:8000
    path('admin/', admin.site.urls),
    path('order/', include('order.urls')),
    path('userinfo/' , include('userinfo.urls')),
    path('' , include('landingpage.urls')),
    path('class/' , include('class.urls')),
]
