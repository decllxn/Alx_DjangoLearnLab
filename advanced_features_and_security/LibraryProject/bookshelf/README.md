# Django Application Setup

## Permissions and User Groups

### Custom Permissions

The following custom permissions have been added to the `Book` model:

- `can_view`: Allows viewing of book details.
- `can_create`: Allows creation of new books.
- `can_edit`: Allows editing of existing books.
- `can_delete`: Allows deletion of books.

These permissions are defined in the `Book` model within the `Meta` class:

```python
class Book(models.Model):
    # Fields here...
    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

