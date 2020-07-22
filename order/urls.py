# urls that are relevant to the order page
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
<<<<<<< HEAD
    path('', views.index , name='order-index'),
    path('summary', views.summary , name='order-summary'),
    
=======
    #path('', views.index , name='order-index'),
    #path('summary', views.summary , name='order-summary'),
    #path('', views.OrderForm.post_new, name='order-index'),
    path('', views.OrderCreate.as_view(), name='order-index'),
>>>>>>> master
]
