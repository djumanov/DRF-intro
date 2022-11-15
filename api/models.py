from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    ram = models.IntegerField()
    price = models.FloatField()

    brand = models.ForeignKey(Company, on_delete=models.CASCADE)