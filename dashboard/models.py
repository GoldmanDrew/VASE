from django.db import models
# Create your models here.managed = True
from django.urls import reverse

class Token(models.Model):
    Name = models.CharField(max_length=255, primary_key = True, null=False)
    Ticker = models.CharField(max_length=4)
    TokenSupply = models.FloatField()
    CashSupply = models.FloatField()
    Price = models.FloatField()
    TimeUpdated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

    class Meta:
        managed = True
        db_table = 'tokens'


class UserShare(models.Model):
    ID = models.AutoField(primary_key = True, null=False)
    User = models.CharField(max_length=255)
    Token = models.ForeignKey(Token, on_delete=models.CASCADE, null=True, db_column="Token")
    Quantity = models.FloatField()

    def __int__(self):
        return self.User

    class Meta:
        managed = True
        db_table = 'UserShares'


class Order(models.Model):
    OrderID = models.AutoField(primary_key = True, null=False)
    User = models.CharField(max_length=255)
    SourceToken = models.ForeignKey(Token, on_delete=models.CASCADE, null=True, related_name="source_token", db_column="SourceToken")
    TargetToken = models.ForeignKey(Token, on_delete=models.CASCADE, null=True, related_name="target_token", db_column="TargetToken")
    Quantity = models.FloatField()
    Filled = models.CharField(max_length=1, null=False)
    OrderTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.OrderID)

    def get_absolute_url(self):
        return "/order/"

    class Meta:
        managed = True
        db_table = 'orders'


class TokenHistory(models.Model):
    ID = models.AutoField(primary_key = True, null=False)
    Token = models.ForeignKey(Token, on_delete=models.CASCADE, null=True, db_column="Token")
    Time = models.DateTimeField(auto_now_add=True)
    Price = models.FloatField()

    class Meta:
        managed = True
        db_table = 'tokenHistory'


class FAQ(models.Model):
    Question = models.TextField()
    Answer = models.TextField()

    class Meta:
        db_table = 'faqs'
