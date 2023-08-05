#Choice fields in django
from django.db import models

class studentData(models.Model):
    city = [
        ('Delhi','Delhi'),
        ('Noida','Noida'),
        ('Other','Other')
    ]
    Rollno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    City = models.CharField(max_length=10, choices=city)
    Fee = models.DecimalField(max_digits=10, decimal_places=2)
