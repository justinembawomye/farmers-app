from django.db import models

# Create your models here.
class Farmer(models.Model):
    GENDER = (
    ('F', 'Female'),
    ('M', 'male'),

    )
    MARRIAGE_STATUS = (
        ('M', 'Married'),
        ('S', 'Single'),

    )
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.CharField(max_length=50)
    marriage_status = models.CharField(max_length=30, choices=MARRIAGE_STATUS)
    telephone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_pictures',default='default.jpg')
    gender = models.CharField(max_length=20, choices=GENDER)
    village= models.CharField(max_length=100)
    community_status = models.CharField(max_length=100)
    instructor_possibility = models.BooleanField(default=True)
    farm_area = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=100)
    past_harvests = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    officer = models.ForeignKey('Officer', on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return "Farmer {} {}".format(self.firstname, self.lastname)

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


