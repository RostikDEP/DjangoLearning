from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos/")
    birthday = models.DateField()