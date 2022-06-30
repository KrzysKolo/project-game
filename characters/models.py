from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Character(models.Model):
    name = models.CharField(max_length=50),
    status = models.CharField(max_length=6),
    death = models.BooleanField(default=False),
    kills = models.IntegerField(),
    description = models.TextField(),
    hp = models.IntegerField(),
    created = models.DateTimeField(auto_now_add=True),
    modified = models.DateTimeField(auto_now_add=True),
    #"id": player_id,
    #   "name": name,
    #    "hp": hp,
    #    "attack": attack,
    #   "status": status,
    #    "death": deaths,
    #    "kills": kills

class Character2(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    sponsored = models.BooleanField(default=False)

class Character3(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=6)
    death = models.BooleanField(default=False)
    kills = models.IntegerField()
    description = models.TextField()
    hp = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
