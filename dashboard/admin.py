from django.contrib import admin
from .models import Token, UserShare, Order

admin.site.register(Token)
admin.site.register(UserShare)
admin.site.register(Order)
