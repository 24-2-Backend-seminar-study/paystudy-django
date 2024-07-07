from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class KakaoPay(models.Model):
    tid=models.CharField(max_length=100)
    partner_order_id=models.CharField(max_length=100)
    partner_user_id=models.CharField(max_length=100)
    point=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    #user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='pay_buyer', null=True)