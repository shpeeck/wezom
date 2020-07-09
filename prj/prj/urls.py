from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from backend.views import *


# drf_yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Delivery API",
        default_version='v1',
        description='''
            Documentation ReDoc viev can be found [here](/doc).
        ''',
        contact=openapi.Contact(email="jenya_vas@mail.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ebd drf_yasg
from rest_framework import routers
from backend.views import CategoryViewSet, AuthView
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)


urlpatterns = [
    path('', include('backend.urls')),
    path('admin/', admin.site.urls),
    path('v1/', include([
        path('generic/', include(router.urls)),
        path('userlogin/', AuthView.as_view)
    ])),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)