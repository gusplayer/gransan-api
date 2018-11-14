# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class post(models.Model):
    class Meta:
        ordering = ('fecha_publicacion',)
    id_user = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    negocio = models.CharField( max_length=256)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento =  models.DateTimeField()
    texto = models.TextField(max_length=2000)
    imagen = models.ImageField(null=True,blank=True,upload_to="estaticos/posts_imagenes/")

    def __str__(self):
        return str(self.texto)