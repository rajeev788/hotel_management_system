from rest_framework import serializers
from .models import * # this astrick includes all  things
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta: #this meta defines extra features
        fields='__all__' #this converts all fields to jason ,you can also use ['title'] to specific field
        model=Invoice

class PayementSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Payment 