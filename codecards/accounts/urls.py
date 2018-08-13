from django.contrib.auth import views
from django.urls import path

app_name='accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]
