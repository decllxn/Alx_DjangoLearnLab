# Django's auth system provides built-in views and utilities for handling user login and logout processes

from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
        path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
]

# In this example, the LoginView class-based view is used to handle user login. the tepmlate_name attribute that specifies the template to be rendered for the login form


