# User registration is the process of creating new user accounts in your application
# Django provides the UserCreationForm and the CreateView class-based view to handle user registration
# This is in the app views.py file


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import Createview


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# In the above example, the SignUpView uses the UserCreationForm to handle user registration.
# When a new user is registered they are redirected to the login page using the success_url
