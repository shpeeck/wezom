from django.urls import path

from backend.views import *


urlpatterns = [
    path('', index),
    path('about', about),
    path('contact', contact)
]