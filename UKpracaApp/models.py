from django.db import models




class User(models.Model):
    userName = models.TextField()
    userSurname = models.TextField()
