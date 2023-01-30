from rest_framework import permissions


class IsAuthorOrStaff(permissions.BasePermission):
    message = "You don't have permission to update or delete this ad"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        else:
            return request.user.role in ["moderator", "admin"]
