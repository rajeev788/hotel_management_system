from django.urls import path
from .views import * 

urlpatterns=[
    path('invoice/all/',InvoiceApiView.as_view()),
    path('invoice/<int:pk>/',InvoiceIdApiView.as_view()),
    path('group/all/',GroupApiView.as_view()),
    path('login/',login),
    path('logout/',logout),
    path('register/',register),

]