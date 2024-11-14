# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .data_access import \
    search as search_data, \
    detail as detail_data, \
    cited as cited_data, \
    related as related_data, \
    category as category_data

from .user_management import \
    login as user_login, \
    register as user_register, \
    update as user_update

# Only needed before data loading.
from .data_load import essay as test_essay_load
from .data_load import edge as test_edge_load


@api_view(['GET'])
def search(request, keyword, page):
    # test_essay_load.load_essay()
    # test_edge_load.load_edge()
    data = search_data.fetch(keyword, page)
    return Response(data)


@api_view(['GET'])
def detail(request, essayId):
    data = detail_data.fetch(essayId)
    return Response(data)


@api_view(['GET'])
def cited(request, essayId):
    data = cited_data.fetch(essayId)
    return Response(data)


@api_view(['GET'])
def related(request, essayId):
    # TODO
    return Response("Hello World!")


@api_view(['GET'])
def category(request, essayId, page):
    data = category_data.fetch(essayId, page)
    return Response(data)


@api_view(['POST'])
def users(request):
    # TODO
    return Response("Hello World!")


@api_view(['POST'])
def login(request):
    email = request.query_params.get('email')
    password = request.query_params.get('password')
    return user_login.check(email, password)


@api_view(['POST'])
def register(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    return user_register.store(name, email, password)


@api_view(['POST'])
def update(request):
    email = request.data.get('email')
    role = request.data.get('role')
    return user_update.store(email, role)
