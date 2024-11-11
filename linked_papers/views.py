# Create your views here.
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    data = {'message': 'Hello, DRF!'}
    return Response(data)