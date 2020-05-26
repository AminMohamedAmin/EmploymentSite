from django.db import models


class file(models.Model):
    """Model containing file field"""
    username = models.CharField(max_length=150, primary_key=True)
    job=models.CharField(max_length=150)
    level=models.IntegerField(default=0)
    file=models.FileField(upload_to="media")