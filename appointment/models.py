from django.db import models

class appointment(models.Model):
    first_name=models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=30,null=True)
    pol = models.CharField(max_length=40,null=True)
    doctor = models.CharField(max_length=40,null=True)
    service = models.CharField(max_length=40,null=True)
    begin = models.TimeField()
    end = models.TimeField()
    comment=models.TextField()
    
