"""
purpose: To create user model to save info.
Author : Pratiksha Mali
"""
from django.db import models

class UserRegistration(models.Model):

    """
    purpose of this class to create model 
    to save user related information in database.
    """
    
    first_name = models.CharField(max_length=25)
    last_name  = models.CharField(max_length=25)
    email      = models.EmailField()
    mobile_no  = models.BigIntegerField()

    def __str__(self):
        return self.first_name