# urls that are relevant to the order page
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    #path('', views.OrderForm.post_new, name='order-index'),
    path('', views.OrderCreate.as_view(), name='order-index'),
]