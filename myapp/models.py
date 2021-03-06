from django.db import models

# Create your models here.
class air_data(models.Model):
    name = models.CharField(max_length=30)
    no_of_flights = models.IntegerField()
    last_service_date = models.DateField(blank=True, null=False, default=None)
    service_required = models.BooleanField(blank=True, null=False, default=False)
    distance_travelled = models.FloatField(blank=True, null=False, default=0)
    base_station = models.CharField(max_length=30)
    accept = models.CharField(max_length=30,default="No")
    image = models.ImageField(upload_to='upload/')
    class Meta:
        db_table="AMS Data"