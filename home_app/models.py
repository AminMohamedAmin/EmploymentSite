from django.db import models

# Create your models here.


class subscribes(models.Model):
    email = models.EmailField(unique=True)