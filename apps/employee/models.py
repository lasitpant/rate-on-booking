from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmployeeManager(models.Model):
    employee = models.ForeignKey(User,related_name="employee_FK",on_delete=models.CASCADE)
    manager = models.ForeignKey(User,related_name="manager_FK",on_delete=models.CASCADE)


class Booking(models.Model):
    user = models.ForeignKey(User,related_name="user_FK",on_delete=models.CASCADE)               # django user object
    booking_type = models.CharField("Booking Type", max_length=10)      # Local/Airport/Outstation
    date = models.CharField("Date", max_length=20)
    time = models.CharField("Time", max_length=10)
    start = models.CharField("Start", max_length=32)
    end = models.CharField("End", max_length=32)
    duration = models.CharField("Time", max_length=20)
    reason =  models.CharField("Reason", max_length=100)
    status = models.SmallIntegerField(default=0)

class TruckOwner(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    email = models.EmailField("Email Address", max_length=50)
    mobile = models.CharField("Mobile Number",max_length=10)