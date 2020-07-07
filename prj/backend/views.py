from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Enterprises, Category, Subcategory, StaticPage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    news = Enterprises.objects.all()
    cat = Category.objects.all()
    subcat = Subcategory.objects.all()
    return render(request, 'frontend/index.html', {'news': news, 'cat': cat, 'subcat': subcat})

def about(request):
    news = StaticPage.objects.all()
    return render(request, 'frontend/about.html', {'news': news})

def contact(request):
    news = StaticPage.objects.all()
    return render(request, 'frontend/contact.html', {'news': news})

def get_category(request, category_id):
    news = Enterprises.objects.filter(subcategory=category_id)
    cat = Category.objects.all()
    subcat = Subcategory.objects.all()
    subctig = Subcategory.objects.get(pk=category_id)
    return render(request, 'frontend/category.html', {'news': news, 'cat': cat, 'subcat': subcat, 'subctig': subctig})
