# Django empowers you to extend or override the default authentication backend to accomodate diverse login methods
# This flexibility allows you to intergrate social login options, two-factor authentication, or any custom authentication flow you desire

# Steps to implementation
# Define a Custom Backend Class
# Create a class that inherits from BaseBackend and implement the authenticate() and get_user() methods. These methods define how user authentication and retrival are handled

from django.contrib.auth.backends import BaseBackend

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        # Implement logic to authenticate user using email and password

    def get_user(self, user_id):
        # Implement logic to retrieve user based on userID

# Register the custom Backend: In the settings.py files, add the path to your custom backend class within the AUTHENTICATION_BACKENDS setting
