from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import book, review
from .serializers import booksSerilizer, reviewsSerilizer
from rest_framework import status

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
    print(allBooks)
    serializers = booksSerilizer(allBooks, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getBook(request, id):
    try:
        result = book.objects.get(id=id)
        serializer = booksSerilizer(result)
        return Response(serializer.data)
    except book.DoesNotExist:
        return Response(status=status.Http_404_NOT_FOUND)
    
@api_view(['GET'])
def getReviewsByBookId(request, id):
    try:
        result = review.objects.filter(book_id=id)
        serializer = reviewsSerilizer(result, many=True)
        return Response(serializer.data)
    except book.DoesNotExist:
        return Response(status=status.Http_404_NOT_FOUND)