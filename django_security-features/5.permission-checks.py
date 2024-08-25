# In views, you can check if a user has a specific permission using the
# user.has_perm() method
# This allows you to control which parts of the view logic are executed based on the user's permissions

def my_view(request):
    if request.user.has_perm('app_name.add_post'):
        # Allow user to create a new post

    else:
        # Deny access or show an error message
