# Permissions and authorizations are a fundamental aspect of web applications security
# They allow you to contorl wwhich users can access specific resources or perform certain actions within your django application
# THis concept explores Django's built-in permission system and how to effectively manage access control

# Permissions - Are fine-grained access controls that define specific actions a user can perform such as "can add post", "can change user", or "can delete comment".

# Groups - Groups allow you to categorize users and design permissions to the enrire group at once. This simplifies permissions management

# Assigning permissions
# Through django admin panel
# or through python scripts

from django.contrib.auth.models import Permission

# Get the permission
permission = Permission.objects.get(codename='add_post')

# Assign permission to a user
user.user_permissions.add(permission)

# Assign permission to a group
group.permissions.add(permission)

