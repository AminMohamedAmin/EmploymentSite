from django.db import models
from django.contrib.auth.models import User
from ee_control_upload.models import file

class SavedCV(models.Model):
    employer = models.CharField(max_length=150)
    employee = models.CharField(max_length=150)
    cv = models.FileField()
    job = models.CharField(max_length=150)


class like(models.Model):
    employer = models.CharField(max_length=150)
    employee = models.CharField(max_length=150)
    cv = models.FileField()
    job = models.CharField(max_length=150)


class dislike(models.Model):
    employer = models.CharField(max_length=150)
    employee = models.CharField(max_length=150)
    cv = models.FileField()
    job = models.CharField(max_length=150)


class love(models.Model):
    employer = models.CharField(max_length=150)
    employee = models.CharField(max_length=150)
    cv = models.FileField()
    job = models.CharField(max_length=150)