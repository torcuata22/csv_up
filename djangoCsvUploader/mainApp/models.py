from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    grades = models.PositiveIntegerField(default = 0)
    roll_number = models.PositiveBigIntegerField(default = 0)
    section = models.CharField(max_length=50)

