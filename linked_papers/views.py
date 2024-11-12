# Create your views here.
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .data_load import essay as t


@api_view(['GET'])
def search(request, keyword, page):
    t.load_essay()
    data = {'message': f'Hello, search! (keyword = {keyword}, page = {page}'}
    return Response(data)


@api_view(['GET'])
def detail(request, essayId):
    data = {'message': f'Hello, detail! (essayId = {essayId})'}
    return Response(data)


@api_view(['GET'])
def cited(request, essayId):
    data = {'message': f'Hello, cited! (essayId = {essayId})'}
    return Response(data)


@api_view(['GET'])
def related(request, essayId):
    data = {'message': f'Hello, related! (essayId = {essayId})'}
    return Response(data)


@api_view(['GET'])
def category(request, categoryName):
    data = {'message': f'Hello, category! (categoryName = {categoryName})'}
    return Response(data)
