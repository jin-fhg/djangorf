from django.db import models
from django.contrib.auth.models import AbstractUser
from geopy.distance import geodesic

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username


class Ride(models.Model):
    status = models.CharField(max_length=50, blank=True, null=True)
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rider', null=True, blank=True)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver', null=True, blank=True)
    pickup_time = models.DateTimeField(auto_now_add=True)
    pickup_latitude = models.FloatField(blank=True, null=True, default=0.0)
    pickup_longitude = models.FloatField(blank=True, null=True, default=0.0)
    dropoff_latitude = models.FloatField(blank=True, null=True, default=0.0)
    dropoff_longitude = models.FloatField(blank=True, null=True, default=0.0)


    def __str__(self):
        return 'Ride {status} {pickupTime}'.format(status=str(self.status),
                                                   pickupTime=str(self.pickup_time))


class Ride_Event(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ride.status + ' ID: ' + str(self.ride.id)


class RideDistance(models.Model):
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE)
    distance = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        pickup_loc = (self.ride.pickup_latitude, self.ride.pickup_longitude)
        dropoff_loc = (self.ride.dropoff_latitude, self.ride.dropoff_longitude)

        self.distance = geodesic(pickup_loc, dropoff_loc).km
        super().save(*args, **kwargs)


