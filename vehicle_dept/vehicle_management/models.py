from django.db import models
from django.core.validators import RegexValidator

#vehicle type specification
vehicle_choice = (
    ("two wheeler","two wheeler"),
    ("three wheeler","three wheeler"),
    ("four wheeler","four wheeler"),
    )

# Create your models here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class vehicle_detail(models.Model):
    vehicle_number = models.CharField(max_length=20,validators=[alphanumeric])
    vehicle_type = models.CharField(max_length = 30, choices =vehicle_choice,default="two wheeler")
    vehicle_model = models.CharField(max_length=20)
    vehicle_desc=models.CharField(max_length=50)
