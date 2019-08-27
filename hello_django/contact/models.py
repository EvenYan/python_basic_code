from django.db import models


# Create your models here.

class PeopleInfo(models.Model):
    name = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name
