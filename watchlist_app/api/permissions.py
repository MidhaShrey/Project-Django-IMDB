from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False

class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permission for read-only methods (GET, HEAD, OPTIONS)
            return True
        else:
            # Check permission for write methods (POST, PUT, PATCH, DELETE)
            return obj.review_user == request.user