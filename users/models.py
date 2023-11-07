from django.db import models
from django.contrib.auth.models import AbstractUser


class UserDetails(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    old_password = models.CharField(max_length=200)


class CourseDetails(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True)
    amount = models.ImageField(max_length=200)
    amount_in_words = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='images/')



# only two tables are added