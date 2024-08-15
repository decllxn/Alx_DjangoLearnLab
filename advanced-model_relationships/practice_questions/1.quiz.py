#!/usr/bin/env python3
# Author - Declan Munene
# Date - 15/08/2024
# Description - A script that creates a model that represents q company with department and employees, using ForeignKey relationships
# Note - This script will not work, it is a mock script used in models.py when working with django

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

class Departments(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')
