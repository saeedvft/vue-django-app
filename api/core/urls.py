from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet

router = DefaultRouter()
router.register('persons', PersonViewSet, basename='person')

urlpatterns = [
    path('api/', include(router.urls)),
]