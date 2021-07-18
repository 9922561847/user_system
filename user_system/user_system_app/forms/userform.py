"""
purpose: Aim of this file is to create required form to save user, admin info
         edit there info.
Author : Pratiksha Mali
"""

from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from user_system_app.models import UserRegistration


class UserRegistrationForm(forms.ModelForm):
    """
    purpose of this class is to create userRegistration form
    as per fields present in UserRegistration Model
    """
    class Meta:
        model = UserRegistration
        fields = '__all__'



class SignUpForm(UserCreationForm):
    """
    this is signup form for user
    """
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class EditUserProfileForm(UserChangeForm):
    """
    user can edit their info using this class password is kept
     manualy none for security purpose
    """
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login','is_active']


class EditAdminProfileForm(UserChangeForm):
    """
    Admin can edit their information using this class,
    since admin have more permissions than user to separate classes are created
    """
    password = None
    class Meta:
        model = User
        fields = '__all__'