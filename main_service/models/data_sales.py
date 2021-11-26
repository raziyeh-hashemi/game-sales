from django.db import models


class DataSales(models.Model):
    rank = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=500)
    platform = models.CharField(null=True, max_length=30)
    year = models.IntegerField(null=True)
    genre = models.CharField(null=False, max_length=20)
    publisher = models.CharField(null=False, max_length=50)
    NA_sales = models.FloatField(null=False)
    EU_sales = models.FloatField(null=False)
    JP_sales = models.FloatField(null=False)
    other_sales = models.FloatField(null=False)
    global_sales = models.FloatField(null=False)
