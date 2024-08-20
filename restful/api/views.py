from django.shortcuts import render
from geopy.distance import geodesic
from django.db.models import FloatField, ExpressionWrapper, F
import math
from rest_framework import viewsets
from .models import Ride, RideDistance
from .serializers import RideSerializer, RideDistanceSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework.filters import OrderingFilter
# Create your views here.

class ResultPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 100
    page_query_param = 'page_num'


class isAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            return False

        if not request.user.is_authenticated:
            return False

        return request.user.role == 'admin'

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('id', 'status', 'rider__email')
    ordering_fields = ['pickup_time']
    pagination_class = ResultPagination
    permission_classes = [isAdmin]

class RideDistanceViewSet(viewsets.ModelViewSet):
    queryset = RideDistance.objects.all()
    serializer_class = RideDistanceSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['distance']
    pagination_class = ResultPagination
    permission_classes = [isAdmin]












