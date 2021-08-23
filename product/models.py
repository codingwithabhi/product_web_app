from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    price = models.IntegerField()
    rating = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product/")
    created = models.DateTimeField(auto_created=True,default=datetime.datetime.now())