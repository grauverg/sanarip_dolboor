from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsNotAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        # if not authenticated, the client can register a new user instance
        elif not request.user or not request.user.is_authenticated:
            return True
        return False
