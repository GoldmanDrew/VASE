from django.db import models
# Create your models here.
from django.urls import reverse


directions = (
    ('A', 'Ask'),
    ('B', 'Bid'),
)
types = (
    ('M', 'Market'),
    ('L', 'Limit'),
)

class Company(models.Model):
    Ticker = models.CharField(max_length=5, primary_key = True, null = False)
    ClassName = models.CharField(max_length=100)
    Department = models.CharField(max_length=50)
    Shares = models.IntegerField()
    ShortFee = models.FloatField(default = 0.00)

    def __str__(self):
        return self.Ticker

    class Meta:
        db_table = 'companies'


class Agent(models.Model):
    id = models.AutoField(primary_key = True, null=False)
    Agent = models.CharField(max_length=20, null = False, unique=True)
    Cash = models.IntegerField(default = 0)
    Wealth = models.IntegerField(default = 0)
    Email = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.Agent

    class Meta:
        db_table = 'agents'


class AgentShare(models.Model):
    id = models.AutoField(primary_key = True, null=False)
    Agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=False)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    Shares = models.IntegerField(default = 0)
    Borrowed = models.IntegerField(default = 0)
    Collateral = models.IntegerField(default = 0)

    def __int__(self):
        return self.Agent

    class Meta:
        db_table = 'agentshares'
        unique_together = (("Agent_id", "Company_id"),)


class Order(models.Model):
    OrderBookName = models.ForeignKey(Company, on_delete=models.CASCADE, null = False)
    Agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    OrderID = models.IntegerField(primary_key=True)
    Type = models.CharField(max_length=1, choices = types)
    Direction = models.CharField(max_length=20, choices = directions)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    QuantityToFill = models.IntegerField()
    Filled = models.CharField(max_length=1, default = 'N')
    IDtoCancel = models.IntegerField()
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.OrderID)


    def get_absolute_url(self):
        return "/order/"

    class Meta:
        db_table = 'orders'

class Price(models.Model):
    OrderBookName = models.CharField(max_length=20)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    DirectionTrigger = models.CharField(max_length=1)
    Asker = models.CharField(max_length=20)
    Asker_OrderID = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='Asker_OrderID', default = None)
    Bidder = models.CharField(max_length=20)
    Bidder_OrderID = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='Bidder_OrderID', default = None)
    BestAsk = models.IntegerField()
    BestBid = models.IntegerField()
    FillID = models.IntegerField(primary_key=True)
    Time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'prices'
