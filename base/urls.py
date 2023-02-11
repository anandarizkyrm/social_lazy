

from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signinPage, name='login'),
    path('signup/', views.signupPage, name='register'),


]
