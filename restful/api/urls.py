from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ride', views.RideViewSet)
router.register(r'distance', views.RideDistanceViewSet)

urlpatterns = [
    path('', include(router.urls), name='ride_page'),
]