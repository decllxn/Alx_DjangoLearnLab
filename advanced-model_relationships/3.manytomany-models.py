# ManytoMany Field represents a many-tomany relationship between two models
# It allows you to associate multiple records from one model with multiple records from another model
# This is useful for modeling hierarchical data structures, such as categories and products, or blog posts and comments

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')

# Each Student can be associated with multiple Course instances, and each Course instance can have multiple Student instances

