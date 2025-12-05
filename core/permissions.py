from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework import permissions


class RoleRequiredMixin(UserPassesTestMixin):
    allowed_roles = []

    def test_func(self):
        user = self.request.user
        if not user.is_authenticated:
            return False
        if user.is_owner():
            return True                           
        return user.role in self.allowed_roles

class OwnerRequiredMixin(RoleRequiredMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_owner()

class CashierRequiredMixin(RoleRequiredMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_cashier()

class SalesAssociateRequiredMixin(RoleRequiredMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_sales_associate()


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_owner()

class IsCashier(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_cashier()

class IsSalesAssociate(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_sales_associate()
