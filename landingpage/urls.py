# urls that are relevant to the landingpage app
from django.urls import path
from . import views

app_name = "landingpage"

urlpatterns = [
    #path('', views.OrderForm.post_new, name='order-index'),
    path('', views.UserFormView.as_view(), name='form-index'),
]
