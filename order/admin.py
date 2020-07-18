from django.contrib import admin
from .models import Company, Agent, AgentShare, Order, Price

# Register your models here.
admin.site.register(Company)
admin.site.register(Agent)
admin.site.register(AgentShare)
admin.site.register(Order)
admin.site.register(Price)
