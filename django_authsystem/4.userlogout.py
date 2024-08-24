from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
        path('logout/', LogoutView.as_view(), name='logout')
]

# The Logout View class-based view is used to handle user logout.When a userlogs out, they are redirected to the default URL specified by the LOGIN_REDIRECT_URL setting
