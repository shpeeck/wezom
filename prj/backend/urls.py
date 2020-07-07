from django.urls import path

from backend.views import *


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('about', about, name='about'),
    path('contact', contact, name='contact')
]