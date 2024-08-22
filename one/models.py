from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Driver(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
    
    
    
class Customerprofile(models.Model):
    user=models.OneToOneField(Customer,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    address=models.TextField(max_length=200)
    phone=models.CharField(max_length=30)
    email=models.EmailField(blank=True)
    picture=models.ImageField(upload_to='customer',blank=True,default='avatar_customer.jpg')   
    
    def __str__(self):
        return self.name 

class Driverprofile(models.Model):
    user=models.OneToOneField(Driver,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=150)
    about=models.CharField(max_length=400,null=True,blank=True)
    place=models.CharField(max_length=100)
    license=models.CharField(max_length=30,blank=True)
    dob=models.DateField(null=True,blank=True)
    phone=models.CharField(max_length=30)
    email=models.EmailField(blank=True)
    exp=models.IntegerField(blank=True)
    availability=models.BooleanField(default=False)
    picture=models.ImageField(upload_to='Driver',blank=True,default='avatar_driver.jpg')
    
    def __str__(self):
        return self.name
    
    
class Bookings(models.Model):
    client=models.ForeignKey(Customerprofile,on_delete=models.CASCADE)
    driver=models.ForeignKey(Driverprofile,on_delete=models.CASCADE)
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    schedule=models.DateField(blank=True)
    
    booked=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{str(self.client)} ~~> {str(self.driver)}'
    
    
class Payment(models.Model):
    booking=models.OneToOneField(Bookings,on_delete=models.CASCADE)
    trans_id=models.CharField(max_length=20,null=True,blank=True)
    amount=models.IntegerField()
    
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.booking)
    

class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    body=models.CharField(max_length=500,null=True,blank=True)
    
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user)