from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    scheduled = models.DateTimeField()
