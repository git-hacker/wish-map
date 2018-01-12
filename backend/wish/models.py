# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class MPUser(models.Model):
    name = models.CharField(max_length=100, blank=True)
    wx_id = models.CharField(max_length=100, blank=True)
    long = models.FloatField(default=0)
    lat = models.FloatField(default=0)

    def __str__(self):
        return self.name


WISH_STATUS = ("待解决", "解决中", "已完成")
WISH_STATUS_CHOICES = zip(WISH_STATUS, WISH_STATUS)

class Wish(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    mp_user = models.ForeignKey(MPUser)
    title = models.CharField(max_length=700)
    detail = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=WISH_STATUS_CHOICES, default=WISH_STATUS_CHOICES[0])
    long = models.FloatField(default=0)
    lat = models.FloatField(default=0)

    def __str__(self):
        return self.title
