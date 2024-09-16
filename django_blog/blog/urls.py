from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', views.index, name='home'),
    # Login view using Django's built-in LoginView
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    
    # Logout view using Django's built-in LogoutView
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    
    # Custom registration view
    path('register/', register_view, name='register'),
    
    # Profile view
    path('profile/', profile_view, name='profile'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),
]
