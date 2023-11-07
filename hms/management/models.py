from django.db import models

# Create your models here.
room_status=[('occupied','occupied'),('not occupied','not occupied'),('not available','not available')]
class room_type(models.Model):
    name=models.CharField(max_length=300)

class room(models.Model):
     room_no=models.CharField(max_length=300)
     floor=models.CharField(max_length=300)
     description=models.CharField(max_length=300)
     bed_count=models.IntegerField()
     status=models.CharField(max_length=300,choices=room_status)
     type=models.ForeignKey(room_type,on_delete=models.SET_NULL,null=True)

