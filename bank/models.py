from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    catergory = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='incomes')


class Expence(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    catergory = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='expences')


