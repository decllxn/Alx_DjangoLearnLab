# This is an example of how a foreign key looks like in a model.py file
from django.db import models

# This is the first model
class Category(models.Model):
    name = models.CharField(max_length=100)

# This is the second model
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, ondelete=models.CASCADE, related_name='products')

# In this example, each Product instance is associated with a single Category instance, while each Category instances have multiple Product instances

