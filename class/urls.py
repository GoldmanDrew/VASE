# urls that are relevant to the order page
from django.urls import path
from . import views

app_name = "class"

urlpatterns = [
    path('', views.classview, name="class-index"),
]
