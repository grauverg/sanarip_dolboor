from rest_framework.permissions import BasePermission, SAFE_METHODS


# permission that checks if the user is authored
class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user == obj.user
        )


class IsAuthorImages(IsAuthor):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user == obj.products.user  # special way to the user
        )


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            # GET, HEAD, OPTIONS methods that do not influence data
            request.method in SAFE_METHODS or
            request.user and
            # is_staff to check if the user is admin
            request.user.is_staff
        )
