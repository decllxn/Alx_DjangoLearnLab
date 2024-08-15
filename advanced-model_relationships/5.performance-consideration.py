# As Data becomes more complex, with multpiple relationships and nested queries, perfomance can become such a concern
# Django provides several tools and techniques to optimize queries involving related objects, such as prefetching and selecting related
# Additionally, prope  indexing and database optimizations can significantly improve query perfomance

## Example
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(model.Models):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

# Optimizing queries with prefetching
products = Product.objects.prefetch_related('category')

# Due to the above  statement, Django will perform a seperate query to fetch all related Category instances, reducing the number of databas  queries and improving perfomance

