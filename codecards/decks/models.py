from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Deck(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='decks')
    updated_at = models.DateTimeField(auto_now=True)
    last_viewed = models.DateField(auto_now=True)


    def __str__(self):
        return self.name
    
    def get_card_count(self):
        return self.cards.count()
    

class Card(models.Model):
    TEXT = 1
    CODE = 2
    CARD_TYPE_CHOICES = (
        (TEXT, 'Text'),
        (CODE, 'Code'),
    )

    card_type = models.PositiveSmallIntegerField(choices=CARD_TYPE_CHOICES, default=TEXT)
    front = models.TextField(null=False)
    back = models.TextField(null=False)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Deck: {self.deck} Card: {self.pk}'

