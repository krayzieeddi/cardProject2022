from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CardType(models.Model):
    cardTypeName=models.CharField(max_length=255)
    cardTypeDescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.cardTypeName
    
    class Meta:
        db_table='cardType'
        verbose_name_plural='cardTypes'

class Card(models.Model):
    cardName = models.CharField(max_length=255)
    cardTypeId = models.ForeignKey(CardType, on_delete = models.DO_NOTHING)
    cardDescription = models.TextField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return self.cardName

    class Meta:
        db_table = 'card'
        verbose_name_plural='cards'