from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import generics, status
from .serializers import UserRegistrationSerializer

from ..models import Product, Address
from .serializers import ProductSerializer, AddressSerializer, OrderSerializer

from django.shortcuts import get_object_or_404

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

@api_view(['GET'])
def getProduct(request, id):

    product = get_object_or_404(Product, id=id)

    serializer = ProductSerializer(product)

    return Response(serializer.data)

@api_view(['GET'])
def getAddressByUserId(request, user_id):
    # Get the address for the specified user ID
    address = get_object_or_404(Address, user_id=user_id)

    # Serialize the address data
    serializer = AddressSerializer(address)

    # Return the serialized data in the response
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
def saveUserAddress(request, user_id):
    try:
        # Check if the user already has an address
        address = Address.objects.filter(user_id=user_id).first()

        if address:
            # If the user has an address, update the existing address
            serializer = AddressSerializer(address, data=request.data)
        else:
            # If the user does not have an address, create a new address
            serializer = AddressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def saveOrder(request):
    try:
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)