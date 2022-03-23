from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getCardTypes/', views.getCardTypes, name='cardTypes'),
    path('getCard/', views.getCard, name='card'),
    path('getCardDetail/<int:id>', views.getCardDetail, name='cardDetail'),
    path('newCard/', views.newCard, name='newCard'),
]