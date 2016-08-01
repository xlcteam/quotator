from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    user = models.ForeignKey(User)
    quote = models.TextField()
    quote_by = models.CharField(max_length=255)


class Quotes(models.Model):
    user = models.ForeignKey(User)
    quotes = models.ManyToManyField(Quote)



