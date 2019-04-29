from django.db import models
import datetime

# Create your models here.
class Farmer(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    village= models.CharField(max_length=100)

    def __str__(self):
        return "Farmer {}".format(self.username)

class Officer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    login_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    district = models.ForeignKey('District', on_delete=models.SET_NULL, null=True)
    subcounty = models.ForeignKey('SubCounty', on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=50)
    

    def __str__(self):
        return " {} {}".format(self.firstname, self.lastname)

class District(models.Model):
    name = models.CharField(max_length=150, default='kampala')     

    def __str__(self):
           return "{}".format(self.name)

class SubCounty(models.Model):
    name = models.CharField(max_length=150, default='kagoma') 

    def __str__(self):
            return "{}".format(self.name)


class Harvest(models.Model):
    name = models.CharField(max_length=150)
    season = models.ForeignKey('Season', on_delete=models.SET_NULL, null=True)
    area = models.CharField(max_length=100)
    Harvest = models.CharField(max_length=50)


class Report(models.Model):
    name = models.CharField(max_length=150)
    season = models.ForeignKey('Season', on_delete=models.SET_NULL, null=True)
    area = models.CharField(max_length=100)
    rice_type= models.CharField(max_length=50)
    sowing_date =models.DateField(default=datetime.date.today)
    sowing_type= models.CharField(max_length=50)
    Planting_type = models.CharField(max_length=50)
    Levelling = models.CharField(max_length=50)
    ridge = models.CharField(max_length=50)
    watercourse_state = models.CharField(max_length=50)
    fertilizers = models.BooleanField(default=True)
    weed_condition = models.CharField(max_length=100)
    harvest_date = models.DateField( default=datetime.date.today)
    total_harvest = models.CharField(max_length=100)
    note =  models.CharField(max_length=200)
    photo = models.ImageField(upload_to='profile_pictures',default='default.jpg')

    def __str__(self):
        return "{}".format(self.name)


class Season(models.Model):
    name = models.CharField(max_length=150, default='planting-season') 

    def __str__(self):
            return "{}".format(self.name)




