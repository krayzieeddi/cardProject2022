from django.shortcuts import render, get_object_or_404
from .models import CardType, Card
from django.urls import reverse_lazy
from .forms import CardForm

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

def newCard(request):
     form=CardForm
     if request.method=='POST':
          form=CardForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=CardForm()
     else:
          form=CardForm()
     return render(request, 'card/newCard.html', {'form': form})