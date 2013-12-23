from rest_framework import permissions

class IsOwnerOrStaff(permissions.BasePermission):
    """Owners and admins have full access, everyone else has no access."""
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.owner == request.user