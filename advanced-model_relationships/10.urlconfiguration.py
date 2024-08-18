# Django's url configuration system allows you to define URL pattersn and map them to corresponding views.
# URL patterns can include parameters and regular expressions to match URL structures.
# The urls.py file in your Django project and apps is where you define these URLpatterns and associate them with the appropriate views

from django.urls import path
from . import views

urlpatterns = [
        path('hello/', views.hello_view, name='hello'),
        path('about/', views.AboutView.as_view(), name='about')
]
