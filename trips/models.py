from django.db import models

# Create your models here.

class GPS_data(models.Model):
    datetime = models.CharField(max_length=100)
    latitude = models.TextField(blank=True)
    longitude = models.TextField(blank=True)
    dic = {'datetime':datetime,
            'latitude':latitude,
            'longitude':longitude}
    def __dic__(self):
        return self.dic