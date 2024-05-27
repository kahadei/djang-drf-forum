from django.contrib.auth.models import User
from django.db import models

from core import settings


# Create your models here.

class Forum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(User, related_name='users', blank=True)


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    body = models.TextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    forum = models.ForeignKey(Forum, related_name='messages', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=1000, blank=True, null=True)
