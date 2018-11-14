# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import post

@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display= ("fecha_publicacion","negocio","texto")
    #exclude = ("fecha_publicacion",)