from django import forms
from .models import CardType, Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'