from django.urls import path
from .views import * 

urlpatterns=[
    path('invoice/all/',InvoiceApiview.as_view()),
    path('invoice/<int:pk>/',InvoiceIdApiview.as_view())

]