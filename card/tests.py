from django.test import TestCase
from django.contrib.auth.models import User
from .models import CardType, Card
import datetime
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

class New_Card_Authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='password1')
        self.type=CardType.objects.create(cardTypeName='Melee')
        self.card=Card.objects.create(cardName='card1', cardTypeId=self.type, cardDescription='thing')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newCard'))
        self.assertRedirects(response, '/accounts/login/?next=/card/newCard/')