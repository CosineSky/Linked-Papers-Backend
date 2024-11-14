import hashlib

from ..models import User
from rest_framework import status
from rest_framework.response import Response


def sha256_hash(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def check(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    if sha256_hash(password) == user.password:
        return Response({
            'message': 'Login successfully.',
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role,
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid password.'}, status=status.HTTP_401_UNAUTHORIZED)
