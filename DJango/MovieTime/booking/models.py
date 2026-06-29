from django.db import models
from django.contrib.auth.models import User
from catalog.models import Movies

#Shows
class Show(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    hall = models.CharField(max_length=50)

#Bookings
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.PositiveIntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)