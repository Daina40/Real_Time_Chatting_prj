from django.db import models
from datetime import datetime

class Room(models.Model):
    name = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'
    

class Message(models.Model):
    value = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=10000)
    user = models.CharField(max_length=10000)

    def __str__(self):
        return f'{self.value} {self.room} {self.user}'