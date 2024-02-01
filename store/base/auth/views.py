from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import generics
from .serializers import UserRegistrationSerializer

from ..models import Product
from .serializers import ProductSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh'
    ]
    return Response(routes)

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

@api_view(['GET'])
def getAllProducts(request):
    # Retrieve all products from the database
    products = Product.objects.all()

    # Serialize the products data
    serializer = ProductSerializer(products, many=True)

    # Return the serialized data in the response
    return Response(serializer.data)