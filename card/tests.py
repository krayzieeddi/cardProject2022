from django.test import TestCase
from django.contrib.auth.models import User
from .models import CardType, Card
from django.urls import reverse_lazy, reverse

# Create your tests here.
class CardTypeTest(TestCase):
    def setUp(self):
        self.type = CardType(cardTypeName = 'cardType1')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'cardType1')

    def test_table(self):
        self.assertEqual(str(CardType._meta.db_table), 'cardType')

class CardTest(TestCase):
    def setUp(self):
        self.type = Card(cardName = 'card1')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'card1')

    def test_table(self):
        self.assertEqual(str(Card._meta.db_table), 'card')