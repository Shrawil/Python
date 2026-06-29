from django.db import models

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    ticket_price = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return (f"{self.name} by {self.producer} on {self.platform} for ${self.ticket_price}!")