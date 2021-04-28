from django.db import models

# Create your models here.
class air_data(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    last_service_date = models.DateField(blank=True, null=False, default=None)
    service_required = models.BooleanField(blank=True, null=False, default=False)
    distance_travelled = models.FloatField(blank=True, null=False, default=0)
    image = models.CharField(max_length=30, blank=True, null=False)
    #to give table name AMS Data
    class Meta:
        db_table="AMS Data"