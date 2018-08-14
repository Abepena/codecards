from django.shortcuts import render, redirect

# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')