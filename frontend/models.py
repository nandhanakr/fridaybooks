from django.db import models


class ContactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class RegistrationDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class CartDB(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    Pname = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)

class CheckoutDB(models.Model):
    PaymentID = models.CharField(max_length=100, null=True, blank=True)
    Orderstatus = models.CharField(max_length=100, null=True, blank=True)
    Amount = models.CharField(max_length=100, null=True, blank=True)
    FirstName = models.CharField(max_length=100, null=True, blank=True)
    LastName = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)

