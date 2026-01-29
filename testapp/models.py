from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=69)
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phnumber=models.BigIntegerField()
    address=models.TextField()