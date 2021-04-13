from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    allow users add thair own profile

    """

    def has_object_permission(self, request, view, obj):
        """
        check user try edit on own profile or not
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
