from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
# Create your models here.


class User(AbstractUser):
    country = CountryField(blank_label='Select Country', default='US')


