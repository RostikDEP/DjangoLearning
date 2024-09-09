from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register),
    path('user/<int:userid>/', userId),
    path('happy_cat/', HappyCat)
]

