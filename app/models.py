from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'


class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.PositiveIntegerField()
    email = models.EmailField()
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cars'