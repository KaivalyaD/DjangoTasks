from django.db import models

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NA', 'None')
]


class User(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Phone = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return self.FirstName
