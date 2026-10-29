from api.models import *
from api.serializers import *
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users, but require authentication for write operations
    # permission_classes = [DjangoModelPermissions]  # Does not allow unauthenticated users to access any endpoints, but allows authenticated users with the appropriate model permissions given by suepruser from admin panel to access the endpoints
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # Allow read-only access for unauthenticated users, but require authentication for write operations


