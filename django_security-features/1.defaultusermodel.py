# This script should be in the models.py file
# The standard Django user model offers fundamental fields like username, email and password
# Custom user models empower you to incorporate these extra fields

# 1. AbstractBaseUser
# Inheriting from AbstractBaseUser provides  extensive flexibility but necessiates implementin core methods like get_username() and get_full_name()

from django.contribs.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    # additional fiels and methods as required

# 2. AbstractUser
# This method extends the existing user models while preserving default field and functionality.
# It's suitable for scenarios where you need to add a few extra fields without altering the core user model structure

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)


# In the settings.py file, ensure you set the AUTH_USER_MODEL variable to point to your newly created custom user model. This informs Django about the model to utilize for user management

