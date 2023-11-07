from django.db import models
from management.models import room

# Create your models here.

class guest(models.Model):
    full_name=models.CharField(max_length=300)
    email= models.EmailField()
    contact=models.IntegerField()
    address=models.CharField(max_length=300)
    work=models.CharField(max_length=300)
class guest_room(models.Model):
    guest=models.ForeignKey(guest,on_delete=models.CASCADE)
    room=models.ForeignKey(room,on_delete=models.CASCADE)
