from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import SignUpForm
# Create your views here.

def signup(request):
    
