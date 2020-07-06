from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Enterprises, Category, Subcategory

# Create your views here.


def index(request):
    news = Enterprises.objects.all()
    cat = Category.objects.all()
    subcat = Subcategory.objects.all()
    return render(request, 'frontend/index.html', {'news': news, 'cat': cat, 'subcat': subcat})

def about(request):
    return render(request, 'frontend/about.html')

def contact(request):
    return render(request, 'frontend/contact.html')

