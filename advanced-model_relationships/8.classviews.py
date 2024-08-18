# Class-based views are an alternative approach to defining views in Django
# They are Python classes that inherit Django's built-in view classes and provide a more structured and reusable way of handling HTTP request
# Class-based views promote:
# - Code reusability
# - Support mixins for shared behavior
# - Offer better organization and seperation of concerns

from django.views generic import TemplateView

class HelloView(TemplateView):
    template_name = 'hello.html'

# Class-based views inherit from various built-in view classed offered by Django
# ListView, DetailView, CreateView
# In the above, the HelloView inherits from Django's TemplateView

