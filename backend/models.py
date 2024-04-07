from django.db import models

# Create your models here.
class CategoryDB(models.Model):
    CName = models.CharField(max_length=100,null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="Images", null=True, blank=True)

class ProductDB(models.Model):
    CName = models.CharField(max_length=100,null=True, blank=True)
    PName = models.CharField(max_length=100,null=True, blank=True)
    Author = models.CharField(max_length=100,null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Price= models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to="Images", null=True, blank=True)