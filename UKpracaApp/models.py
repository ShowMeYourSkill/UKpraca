from django.db import models




class User(models.Model):
    name = models.TextField()
    surname = models.TextField()
    experience = models.TextField()
    preferences = models.TextField()
