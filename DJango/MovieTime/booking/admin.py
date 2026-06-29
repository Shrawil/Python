from django.contrib import admin
from .models import Show, Booking

admin.site.register(Booking)
admin.site.register(Show)