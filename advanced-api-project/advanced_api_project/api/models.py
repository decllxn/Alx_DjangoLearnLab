from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=25)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Author')

