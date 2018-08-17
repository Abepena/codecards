from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .models import Category

# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    #TODO: return render(request, 'profile.html') 
    pass

class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"