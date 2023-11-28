from rest_framework import serializers
from .models import * # this astrick includes all  things
from django.contrib.auth.models import Group
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta: #this meta defines extra features
        fields='__all__' #this converts all fields to jason ,you can also use ['title'] to specific field
        model=Invoice

class PayementSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Payment 

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields=['id','name']
        model=Group


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields= ['email','password','groups']
        model=User