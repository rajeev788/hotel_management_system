from django.db import models
from frontdesk.models import guest
from django.contrib.auth.models import AbstractUser 
# Create your models here.
invoice_status=[('paid','paid'),('not paid','not paid')]

class User(AbstractUser):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=300)
    username=models.CharField(max_length=300,null=True,default='user')

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

class Invoice(models.Model):
    guest=models.ForeignKey(guest,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=300)
    amount=models.IntegerField()
    status=models.CharField(max_length=300,choices=invoice_status)
class Payment(models.Model):
    Invoice=models.OneToOneField(Invoice,on_delete=models.CASCADE)
    amount=models.IntegerField()