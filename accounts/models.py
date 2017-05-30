from django.db import models
from .managers import User_GroupManager
from django.contrib.auth.models import User


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to = 'avatars/', default = 'avatars/default.jpg')
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    rep = models.IntegerField(default=0)
    slug = models.CharField(unique=True, max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ForeignKey(Avatar, null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    public = models.BooleanField(default = False)
    display_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.slug

class User_Group(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    users = models.ManyToManyField(User, related_name='user_groups')
    public = models.BooleanField(default = False)
    avatar = models.ImageField(upload_to = 'avatars/', default = 'avatars/default.jpg')

    objects = User_GroupManager()

    def __str__(self):
        return self.slug