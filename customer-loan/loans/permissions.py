from rest_framework.permissions import BasePermission
class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self,request,view,object):
        if request.user.is_staff:
            return True
        return object.user==request.user