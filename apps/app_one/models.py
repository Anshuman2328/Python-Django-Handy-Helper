from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["fname"] = "First name should be at least 2 characters"
        if not (postData['fname']).isalpha():
            errors["fname_alpha"] = "First name should be only letters"
        
        if len(postData['lname']) < 2:
            errors["lname"] = "Last name should be at least 2 characters"
        if not (postData['lname']).isalpha():
            errors["lname_alpha"] = "Last name should be only letters"
        
        if not EMAIL_REGEX.match(postData['email']):
           errors["email"] = "Please enter a valid email"
        
        potential_matches = self.filter(email=postData['email'])
        if len(potential_matches) > 0:
            errors["email_uniqueness"] = "Email already exists"

        if len(postData['password']) < 2:
            errors["password"] = "Password should at least be 8 characters"

        if postData['confirmpw'] !=postData['confirmpw']:
            errors['conf'] = "Passwords do not match"
        
        return errors


class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()



    def __repr__(self):
        return f'Name of the User is {self.fname}{self.lname} and the email is {self.email}'
