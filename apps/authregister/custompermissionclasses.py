from rest_framework.permissions import BasePermission

class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.__class__.__name__ != "Admins":
            return None
        else:
            return True

class CustomersPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.__class__.__name__ != "Customers":
            return None
        else:
            return True

class MechanicsPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.__class__.__name__ != "Mechanics":
            return None
        else:
            return True

class ReceptionistPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.__class__.__name__ != "Receptionist":
            return None
        else:
            return True
