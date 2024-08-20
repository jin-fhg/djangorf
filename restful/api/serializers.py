from rest_framework import serializers
from .models import Ride, User, Ride_Event, RideDistance
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'role')


class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride_Event
        fields = '__all__'


class RideDistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideDistance
        fields = '__all__'
        depth = 1



class RideSerializer(serializers.ModelSerializer):
    todays_ride_events = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Ride
        fields = ('status', 'rider', 'driver', 'pickup_time', 'pickup_latitude',
                  'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude',
                  'todays_ride_events', 'distance')
        depth = 1

    def get_todays_ride_events(self, obj):
        today_start = timezone.now().date()
        today_end = today_start + timezone.timedelta(days=1)
        result = obj.ride_event_set.filter(created_at__gte=today_start,
                                        created_at__lt=today_end)
        return RideEventSerializer(result, many=True).data


    def get_distance(self, obj):
        related = RideDistance.objects.get(ride_id=obj.id)
        if not related:
            new_distance = RideDistance.objects.create(ride_id=obj.id)
            return new_distance.distance
        return related.distance




