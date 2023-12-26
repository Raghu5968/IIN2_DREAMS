from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employees(models.Model):
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE,related_name='employees')
    empname=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100)
    number=models.CharField(max_length=10,null=True)
    password=models.CharField(max_length=100)
    profile_pic=models.ImageField(default="pic.png",null=True,blank=True)
    def __str__(self):
        return self.empname
    
class Check_in(models.Model):
    check_in_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=100)

class TimeSheet(models.Model):
    empname = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=50)
    day = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.emp_name} - {self.day} {self.time}"
    


