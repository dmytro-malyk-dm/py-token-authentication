from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


class ListCreatePermissionMixin:

    def get_permissions(self):
        if self.action in ("list", "create"):
            return [
                permission() for permission in self.permission_classes
            ]
        return []

    def retrieve(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

    def update(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

    def partial_update(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

    def destroy(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )


class ListCreateRetrievePermissionMixin:
    def get_permissions(self):
        if self.action in ("list", "create", "retrieve"):
            return [
                permission() for permission in self.permission_classes
            ]
        return [IsAdminUser()]

    def update(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def partial_update(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def destroy(self, request, *args, **kwargs):
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
