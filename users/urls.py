from django.contrib.auth import login
from django.urls import path
from django.contrib.auth.views import LoginView
import users
from . import views


def auth_views(args):
    pass


app_name = 'users'

urlpatterns = [
    path('users/login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('users/register/', views.register, name='register'),

]
