from django.shortcuts import render, get_object_or_404
from .models import CardType, Card

# Create your views here.
def index(request):
    return render(request, 'card/index.html')

def getCardTypes(request):
    cardType_list=CardType.objects.all()
    return render(request, 'card/cardTypes.html' ,{'cardType_list' : cardType_list})

def getCard(request):
    card_list=Card.objects.all()
    return render(request, 'card/card.html' ,{'card_list' : card_list})

def getCardDetail(request, id):
    card = get_object_or_404(Card, pk=id)
    cardDetails = card.cardDescription
    context = {
        'card' : card,
        'cardDetails' : cardDetails,
    }
    return render(request, 'card/cardDetail.html', context=context)
