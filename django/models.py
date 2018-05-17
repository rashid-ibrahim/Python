from django.db import models

class Customer(models.Model):
    customer = models.CharField(max_length=20)
    cust_since = models.DateTimeField('customer since')

class FirstName(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    
class LastName(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=20)
    
class PhoneNumber(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=20)