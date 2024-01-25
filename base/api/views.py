from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import book
from .serializers import booksSerilizer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    allBooks = book.objects.all()
    serializers = booksSerilizer(allBooks, many=True)
    return Response(serializers.data)