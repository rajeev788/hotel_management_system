from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Invoice
from rest_framework.response import Response
from .serializers import *
@api_view(['GET'])
def invoice(request):
    queryset = Invoice.objects.all()
    serializer=InvoiceSerializer(queryset,many=True)
    return Response(serializer.data)