from django.db import models
from django.contrib.auth.models import User
from baseapp.models import *
class clinic(models.Model):
    name = models.CharField(max_length=100, null=True)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    adress = models.CharField(max_length=100, null=True)
    orientir = models.CharField(max_length=100, null=True)
    latitude = models.FloatField(("Kenglik"), blank=True, null=True)
    longitude = models.FloatField(("Uzunlik"), blank=True, null=True)
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class user(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=30,null=True)
    adress = models.CharField(max_length=100, null=True)
    birthday = models.DateField()
    image=models.ImageField()
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    specialty = models.CharField(max_length=30, null=True)
    experience = models.CharField(max_length=30, null=True)
    worktime_begin = models.TimeField()
    worktime_end = models.TimeField()
    is_fullday = models.BooleanField()
    clinic = models.ForeignKey(clinic,on_delete=models.CASCADE)
    def __str__(self):
        return self.user_id.first_name + '' + self.user_id.last_name
    @property
    def ImageURL(self):
        return self.image.url
    @property
    def Name(self):
        return self.user_id.last_name + ' ' +self.user_id.first_name
class cabinet_photo(models.Model):
    image=models.ImageField()
    dentist=models.ForeignKey(user,on_delete=models.CASCADE)
class service(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(default=0)
    duration = models.IntegerField()
    dentist = models.ForeignKey(user,on_delete=models.CASCADE)







