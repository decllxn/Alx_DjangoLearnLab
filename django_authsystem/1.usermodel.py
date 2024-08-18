# Django comes with a built-in authentication system that provides a set of models, views and utilities for handling user authentication

# 1. User Model
# The user model serveed as the foundation for representing a user within the
# authentication system.
# It stores essential user information such as username, password(hashed for security), email address, and other relevant user-related data

from django.contrib.auth.models import User

# Create new user
user = User.objects.create_user('john', 'john@example.com', 'password123')

# Retrieve a user based on username
user = User.objects.get(username='john')

# 2. Authentication Middleware
# Django incorporates authentication middleware that seamlessly associates users with incoming requests and grants access to the authenticated user within views and templates


