from django.db import models

# Create your models here.

class Product(models.Model):
    name =  models.CharField( max_length=255)#contain textuel data
    price= models.FloatField(())#contains float
    stock=models.IntegerField()#contains integer
    image_url=models.CharField(max_length=2083) 

class Offer( models.Model): #class to define a coupon 
    code =  models.CharField(max_length=10)
    description = models.CharField( max_length=250)
    discount = models.FloatField()
