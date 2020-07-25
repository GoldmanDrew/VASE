# urls that are relevant to the order page
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path('', views.orderpage, name="order-index"),
]
