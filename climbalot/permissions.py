from rest_framework import permissions
from climbalot.models import Monkey

class IsUserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj=None):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.player == request.user

class IsMonkeyOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        player_id = request.user
        monkey = Monkey.objects.get(player = player_id)
        return obj.monkey == monkey
