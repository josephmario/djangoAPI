from django.db import models

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.firstname + ' ' + self.middlename + ' ' + self.lastname