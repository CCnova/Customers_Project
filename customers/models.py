from django.db import models

from customers.utils.geolocation_utils import getGeolocationFromAddress


# Create your models here.
class Customer(models.Model):
  GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.EmailField()
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  company = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  latitude = models.FloatField(null=True)
  longitude = models.FloatField(null=True)

  def save(self, *args, **kwargs):
    geolocation = getGeolocationFromAddress(self.city)
    self.latitude = geolocation['latitude']
    self.longitude = geolocation['longitude']
    super().save(*args, **kwargs)

  def __str__(self):
    return f'''
      Name: {self.first_name} {self.last_name}
      Email: {self.email}
      Title: {self.title}
      Company: {self.company}
      Location: {self.latitude} - {self.longitude}
    '''
