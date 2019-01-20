from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from datetime import datetime
from ..app_one.models import *
# Create your models here.

class WorkManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors['title'] = 'Please enter a title (greater than 3 letters) for the job'
        if len(postData['destination']) < 3:
            errors['destinationlength'] = "Location cannot be blank. Please input valid entry."
        if len(postData['description']) < 8:
            errors['descriptionlength'] = "Description about work must be more than 8 letters. Please input valid entry."
        # if len(postData['start_date']) < 1:
        #     errors['startlength'] = "Start date cannot be blank. Please input valid entry."
        # elif postData['start_date'] < str(datetime.now()):
        #     errors['paststart'] = "Start date should be a future date."
        # if len(postData['end_date']) < 1:
        #     errors['endlength'] = "This field must not be blank."
        # elif postData['end_date'] < str(datetime.now()):
        #     errors['pastend'] = "End date must be in the future."
        # if postData['start_date'] > postData['end_date']:
        #     errors['dateerror'] = "Start date must be before the end date."
        return errors

class Work(models.Model):
    title = models.CharField(max_length = 45)
    # user_name = models.CharField(max_length = 45)
    destination = models.CharField(max_length = 255)
    description = models.TextField()
    # start_date = models.DateTimeField()
    # end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user_created = models.ForeignKey(User, related_name = "job_created", on_delete='models.CASCADE')
    user_travelling = models.ManyToManyField(User, related_name = "jobs_by_users")
    objects = WorkManager()
