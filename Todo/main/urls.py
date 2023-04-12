from django.urls import path

from . import views

urlpatterns= [

path('', views.home),
path('html/',views.Html),
path('details/<str:id>' ,views.details , name='details' ),
path('create/',views.create, name='create'),
path('update/<str:pk>' ,views.update, name='update' ),



]