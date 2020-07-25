# urls that are relevant to the userinfo app
from django.urls import path
from . import views

app_name = "userinfo"

urlpatterns = [
    path('', views.agentDisplay, name="userinfo-display"),
    # path('' , views.sharesDisplay, name = "agent-shares-display"),
]
