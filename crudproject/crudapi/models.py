from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
