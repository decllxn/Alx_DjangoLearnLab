from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # Login view using Django's built-in LoginView
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Logout view using Django's built-in LogoutView
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    
    # Custom registration view
    path('register/', register_view, name='register'),
    
    # Profile view
    path('profile/', profile_view, name='profile'),
]
