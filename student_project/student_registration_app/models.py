# models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100,unique=True,default='')
    email = models.EmailField(unique=True,default='')
    phone_number = models.CharField(unique=True,max_length=10,default='')
    date_of_birth = models.DateField(default='2000-10-10')
    address = models.CharField(default='',max_length=1000)
    password = models.CharField(max_length=100,default='')
    Confirm_password = models.CharField(max_length=100,default='')
    

    def __str__(self):
        return self.name

