from django.shortcuts import render
from .models import CardType, Card

# Create your views here.
def index(request):
    return render(request, 'card/index.html')

def getCardTypes(request):
    cardType_list=CardType.objects.all()
    return render(request, 'card/cardTypes.html' ,{'cardType_list' : cardType_list})