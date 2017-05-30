from __future__ import unicode_literals

from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Colors(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    color = ColorField(default='#FF0000')
    secondary_color = ColorField(default='#FFFF00')
    third_color = ColorField(default='#FFFFFF')
    def __str__(self):
        return self.title


