from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    amount = models.DecimalField()
    catergory = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='incomes')


class Expence(models.Model):
    amount = models.DecimalField()
    catergory = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='expences')


