from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    """
    Custom permission class that allows access based on user roles.
    """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True  # Allow read-only access for all users
        return False