from django.db import models

# Create your models here.
class air_data(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    age=models.IntegerField()
    #to give table name AMS Data
    class Meta:
        db_table="AMS Data"