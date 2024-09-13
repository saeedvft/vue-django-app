from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.family_name}"

