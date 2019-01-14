# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=100, null=False)
    message = models.CharField(max_length=300, null=False)
    author = models.CharField(max_length=100, null=False)

