from django.db import models

# Create your models here.
class menu(models.Model):
    menu_name=models.CharField(max_length=300)

class food(models.Model):
    name=models.CharField(max_length=300)
    description =models.CharField(max_length=300)
    menu=models.ForeignKey(menu,on_delete=models.SET_NULL,null=True) 