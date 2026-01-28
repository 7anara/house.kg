from rest_framework import permissions
from .models import *


class CheckBuyer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'buyer'


class CheckSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'seller'