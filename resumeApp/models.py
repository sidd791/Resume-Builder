from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    ph_num = models.CharField(max_length = 12)
    education = models.TextField(max_length = 2000)
    degree = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)   
    experience = models.TextField(max_length = 2000)
    hobbies = models.CharField(max_length=100)
    def __str__(self):
        return self.name