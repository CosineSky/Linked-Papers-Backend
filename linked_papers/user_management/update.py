import hashlib
from ..models import User
from rest_framework import status
from rest_framework.response import Response


def sha256_hash(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def store(email, role):
    user = User.objects.filter(email=sha256_hash(email)).update(role=role)
    return Response({
        'message': 'Update successfully.',
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'role': user.role,
    }, status=status.HTTP_200_OK)
