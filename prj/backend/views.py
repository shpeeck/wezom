from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Enterprises, Category, Subcategory, StaticPage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from rest_framework import serializers
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

class CommonResponceSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()

class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthView(APIView):
    """
        User login.
    """
    @swagger_auto_schema(
        request_body = LoginRequestSerializer,
        responses= { 200:  CommonResponceSerializer}
    )
    def post(self, request):
        return Response(CommonResponceSerializer({
            'status': 0,
            'message': 'Goooood'
        }).data)


from rest_framework.decorators import api_view

@api_view()
def hello(request):
    return Response({"message": "hello"})

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to read and modify categories.
    """
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post']


def index(request):
    newses = Enterprises.objects.all()

    # paginator
    paginator = Paginator(newses, 16)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    # end paginator

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
    newses = Enterprises.objects.filter(subcategory=category_id)

    # paginator
    paginator = Paginator(newses, 16)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    # end paginator

    cat = Category.objects.all()
    subcat = Subcategory.objects.all()
    subctig = Subcategory.objects.get(pk=category_id)
    return render(request, 'frontend/category.html', {'news': news, 'cat': cat, 'subcat': subcat, 'subctig': subctig})
