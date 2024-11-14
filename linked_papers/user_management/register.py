import hashlib
from ..models import User
from rest_framework import status
from rest_framework.response import Response


def sha256_hash(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def store(name, email, password):
    user = User.objects.create(
        name=name,
        email=sha256_hash(email),
        password=sha256_hash(password),
        identity=False,
    )
    return Response({
        'message': 'Register successfully.',
        'id': user.id,
        'name': user.name,
        'email': user.email,
    }, status=status.HTTP_200_OK)
