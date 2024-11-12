# Create your views here.
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .data_access import \
    search as search_data, \
    detail as detail_data, \
    cited as cited_data, \
    related as related_data, \
    category as category_data

# Only needed before data loading.
from .data_load import essay as test_essay_load
from .data_load import edge as test_edge_load


@api_view(['GET'])
def search(request, keyword, page):
    test_essay_load.load_essay()
    test_edge_load.load_edge()
    data = search_data.fetch(keyword, page)
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
