from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser

from .models import Deck

# Create your views here.

# class HomeView(ListView):
#     model = Deck
#     context_object_name = 'decks'
#     template_name = 'home.html'

    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['decks'] = Deck.objects.filter(created_by=self.request.user)

def home(request):
    if request.user.is_authenticated:
        decks = Deck.objects.filter(created_by=request.user).order_by('-created_at')
    else:
        decks = {}
    return render(request, 'home.html', {"decks": decks})

def profile(request):
    #TODO: return render(request, 'profile.html') 
    pass

