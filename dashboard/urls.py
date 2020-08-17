# urls that are relevant to the order page
from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.classview, name="dashboard-index"),
    path('get_prices', views.priceview, name="dashboard-getprice"),
]
