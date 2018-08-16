from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """
    params:name, description, owner (User)
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories' )

    def __str__(self):
        return self.name

class Deck(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='decks')
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='decks')

    def __str__(self):
        return self.name
    
    

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

