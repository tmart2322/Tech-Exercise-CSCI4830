from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return self.title
