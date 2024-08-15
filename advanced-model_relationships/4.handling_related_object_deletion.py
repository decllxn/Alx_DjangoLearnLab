# When working with related objects, it is important to manage their deletion behavior
# Django provides several options for handling object deletion, such as CASCADE
# CASCADE(deleting related objects automatically)
# PROTECT(preventing deleted objects if related objects exists)
# SET_NULL(setting the related field to NULL)
# SET_DEFAULT(setting the related field to a default value)

## Example
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

# In the above example, if an AUthor is deleted, all associated Book instances will also be automaticaly deleted due to the on_delete=models.CASCADE
