# urls that are relevant to the order page
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path('', views.orderpage, name="order-index"),
    path('cancel_order/<int:pk>/', views.cancelorder, name="cancel_order"),
    path('postorder/', views.postorder, name = "post_order"),
    path('yourorders/', views.yourorders, name="your_orders"),
    path('allorders/', views.allorders, name="all_orders"),
    path('gotoorder/<str:className>/', views.goToOrder, name="goto_order"),
    path('orderfilter/', views.orderfilter, name="order_filter"),
    path('activefilter/', views.activefilter, name="active_filter"),
]
