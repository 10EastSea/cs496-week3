# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Answer(models.Model):
    question_number = models.IntegerField()
    answer = models.IntegerField()

class User(models.Model):
    userID = models.TextField()
    userPW = models.TextField()
    mbti = models.TextField()

class Song(models.Model):
    title = models.TextField()
    url = models.TextField()
    thumbnail = models.TextField()