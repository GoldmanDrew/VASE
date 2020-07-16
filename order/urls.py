# urls that are relevant to the order page
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='order-index'),
    path('summary', views.summary , name='order-summary'),
]
