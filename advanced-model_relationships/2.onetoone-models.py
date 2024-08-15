# A OneToOne Field represents a one-to-one relationship between two models
# A OnetoOneField represents a one-to-one relationship between two models. It ensure  that a record from one model is associated with at most one record of another model and viceversa

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
