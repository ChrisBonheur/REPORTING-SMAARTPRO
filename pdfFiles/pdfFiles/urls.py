
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, routers

schema_view = get_schema_view(
    openapi.Info(
        title="REPORTING API",
        default_version='v1',
        description="api For reporting",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="admin@zandosoft.com"),
        license=openapi.License(name=""),
    ),
    public=True,
)

router = routers.SimpleRouter()

urlpatterns = [
    path('smaartpro/', include('smaartpro.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),
]
