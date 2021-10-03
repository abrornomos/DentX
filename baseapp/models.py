from django.db import models
from django.utils.translation import ugettext_lazy as _
class Language(models.Model):
    name=models.CharField(("Til nomi"),max_length=30)
    def __str__(self):
        return self.name
class Gender(models.Model):
    name_g=models.CharField(("Jinsi"),max_length=30)

    def __str__(self):
        return self.name_g
class Region(models.Model):
    reg_name=models.CharField(('Hudud nomi'),max_length=30)

    def __str__(self):
        return self.reg_name


