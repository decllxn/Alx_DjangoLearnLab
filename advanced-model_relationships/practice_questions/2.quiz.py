#!/usr/bin/env python3
# Author - Declan Munene
# Date - 15/08/2024
# Description - A script that creates a model for a productand it's detaile ddescription using OneToOneField

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self.name):
        return f"{self.name}"

class Description(models.Model):
    designer = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='description')
