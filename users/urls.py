from django.contrib.auth import login
from django.urls import path
from . import views


urlpatterns = [
    path('login/', login, {'template_name': 'users/login.html'}, name='login')
]
