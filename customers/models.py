from django.db import models


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
