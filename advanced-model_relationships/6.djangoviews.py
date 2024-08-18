# views are used to handle HTTP request s and generate responses
# There are two types of views:
# Class-based views
# Function-based views
# Views are Python Functions or Classes that receive HTTP requests, process the data, and return HTTP responses.

# Function-Based Views
# Function-based views are the traditional way of defining views in Django. The
# They are Pythins functions that take an HTTP request and return an HTTP response.
# Function-based vies are straightforward and easy to understand.

from django.http import HttpResponse

def hello_view(request):
    # A basic function view returning a greeting message
    return HttpResponse("Hello, World!")
