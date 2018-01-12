# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib import admin

from .models import MPUser, Wish


@admin.register(MPUser)
class MPUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'wx_id', 'long', 'lat')


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('title', 'mp_user', 'status', 'long', 'lat', 'created', 'detail')
