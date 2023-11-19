from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Invoice
from rest_framework.response import Response
from .serializers import *
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404 #this 404 is data not found response
from rest_framework.permissions import IsAuthenticated
'''
@api_view(['GET','POST']) #this done by using function but this can be also done by using class which is doen under
def invoice(request):
    if request.method=='GET':
        queryset = Invoice.objects.all()
        serializer=InvoiceSerializer(queryset,many=True) #this many = true is to serialoze multiple objects
        return Response(serializer.data)
    else:
        data= request.data
        serializer=InvoiceSerializer(data=data)
        if serializer.is_valid(): #this is_valid checks if the value passed is valid or not
            serializer.save()
            return Response('data created')
        else:
            return Response(serializer.errors)
'''
@api_view(['POST'])
def login(request):
        pass
class InvoiceApiview(GenericAPIView):
    permission_classes=[IsAuthenticated] #this is for the permission

    def get(self,request):
        queryset = Invoice.objects.all()
        serializer=InvoiceSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request):
        data= request.data
        serializer=InvoiceSerializer(data=data)
        if serializer.is_valid(): #this is_valid checks if the value passed is valid or not
            serializer.save()
            return Response('data created')
        else:
            return Response(serializer.errors)

class InvoiceIdApiview(GenericAPIView):
    permission_classes=[IsAuthenticated] 

    def get_queryset(self,pk): 
        object=get_object_or_404(Invoice,id=pk)
        return object

    def get(self,request,pk):
        object=self.get_queryset(pk)
        serializer=InvoiceSerializer(object) #here we donot use many = true because it only serialize only one objects
        return Response(serializer.data)
    
    def put(self,request,pk):
       object=self.get_queryset(pk)
       serializer=InvoiceSerializer(object,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response('data updated')
       else:
           return Response(serializer.errors)
    def patch(self,request,pk):
       object=self.get_queryset(pk)
       serializer=InvoiceSerializer(object,data=request.data,partial=True)
       if serializer.is_valid():
            serializer.save()
            return Response('data updated')
       else:
           return Response(serializer.errors)
       
    def delete(self,request, pk):
        object=self.get_queryset(pk)
        object.delete()
        return Response('data deleted')

 

     