from django.db import models
from django.db import models
from django.contrib.auth.models import User
from baseapp.models import *
from dentist.models import *
class patent(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=30,null=True)
    adress = models.CharField(max_length=100, null=True)
    birthday = models.DateField()
    image = models.ImageField()
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    def __str__(self):
        return self.user_id.first_name + ' ' +self.user_id.last_name
    @property
    def Name(self):
        return self.user_id.first_name + ' ' +self.user_id.last_name
    @property
    def ImageUrl(self):
        return self.image.url
class tooth(models.Model):
    code = models.IntegerField()
    status = models.CharField(max_length=200,null=True)
    patient = models.ForeignKey(patent,on_delete=models.CASCADE)
class notification(models.Model):
    sender = models.ForeignKey(user,on_delete=models.CASCADE)
    recipient = models.ForeignKey(patent,on_delete=models.CASCADE)
    message = models.TextField()
class plan(models.Model):
    name = models.CharField(max_length=100)
    is_done = models.BooleanField()
    patient = models.ForeignKey(patent,on_delete=models.CASCADE)
class photo(models.Model):
    image = models.ImageField()
    patient = models.ForeignKey(patent, on_delete=models.CASCADE)



