from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    work = models.ManyToManyField('Work', blank=True)

    def __str__(self):
        return self.name

class Work(models.Model):
    link = models.CharField(max_length=100)
    YOUTUBE = 'youtube'
    INSTAGRAM = 'instagram'
    OTHER = 'other'
    WORK_TYPE_CHOICES = [
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    ]
    work_type = models.CharField(
        max_length=10,
        choices=WORK_TYPE_CHOICES,
        default=OTHER,
    )

    def __str__(self):
        return self.name