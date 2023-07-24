from rest_framework import permissions
# from snippets.permissions import IsOwnerOrReadOnly

class IsOwnerOrReadOnly(permissions.BasePermission):
    """ 控制对象级别权限 """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

        