from django.contrib import admin
from .models import Token, UserShare, Order, TokenHistory

admin.site.register(Token)
admin.site.register(UserShare)
admin.site.register(Order)
admin.site.register(TokenHistory)
