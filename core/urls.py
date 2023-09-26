"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import DutyPlaceViewSet, DutyTimeViewSet, SecurityGuardDutyTimeListView, SecurityGuardViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
router.register(r'security-guards', SecurityGuardViewSet)
router.register(r'duty-places', DutyPlaceViewSet)
router.register(r'duty-times', DutyTimeViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API Docs",
        default_version='v1',
        description='''This Api : 
        - Register security guard (name, surname, date of birth, years of experience)
        - Assign Duty Time (for example, Morning 9 am to 6 pm, override control should be done)
        - List page of security guards registers when clicked duty time should be shown.
          ''',
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('security-guards/<int:pk>/duty-times/', SecurityGuardDutyTimeListView.as_view(), name='security-guard-duty-times'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
