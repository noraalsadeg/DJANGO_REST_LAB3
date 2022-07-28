from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=512)
    lastName = models.CharField(max_length=512)
    birthDate = models.DateField()
    GPA = models.FloatField()