from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import generics, status
from .serializers import UserRegistrationSerializer

from ..models import Product, Address, Order, Review, CustomUser
from .serializers import ProductSerializer, AddressSerializer, OrderSerializer, ReviewSerializer

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
        user_id = request.data.get('user')
        products_data = request.data.get('products', [])

        # Validate user and products_data
        if not user_id or not products_data:
            return Response({'error': 'Invalid request data'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Iterate over products and create Order records
        order_records = []
        for product_data in products_data:
            product_id = product_data.get('product')
            product_quantity = product_data.get('product_quantity')

            # Validate product data
            if not product_id or not product_quantity:
                return Response({'error': 'Invalid product data'}, status=status.HTTP_400_BAD_REQUEST)

            # Create Order record
            order_data = {
                'user': user_id,
                'product': product_id,
                'product_quantity': product_quantity,
                'status': 'pending'
            }
            order_serializer = OrderSerializer(data=order_data)
            if order_serializer.is_valid():
                order_serializer.save()
                order_records.append(order_serializer.data)
            else:
                return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(order_records, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['GET'])
def getUserOrders(request, user_id):
    try:
        # Get the user's address details
        user_address = get_object_or_404(Address, user_id=user_id)
        address_serializer = AddressSerializer(user_address)
        
        # Get all orders for the specified user ID
        orders = Order.objects.filter(user_id=user_id)

        # Serialize the orders data
        order_serializer  = OrderSerializer(orders, many=True)

        # Include both orders and user address details in the response
        response_data = {
            'user_address': address_serializer.data,
            'user_orders': order_serializer.data
        }

        # Return the serialized data in the response
        return Response(response_data)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def saveReview(request):
    try:
        user_id = request.data.get('user_id')
        product_id = request.data.get('product_id')
        review_text = request.data.get('review')

        # Validate user, product, and review_text
        if not user_id or not product_id or not review_text:
            return Response({'error': 'Invalid request data'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user and product exist
        user = get_object_or_404(CustomUser, id=user_id)
        product = get_object_or_404(Product, id=product_id)

        # Get or create the user and product instances
        user = CustomUser.objects.get(pk=user_id)
        product = Product.objects.get(pk=product_id)

        # Create Review record
        review_data = {
            'user': user_id,
            'product': product_id,
            'review': review_text,
        }
        review_serializer = ReviewSerializer(data=review_data)

        # Check if the user already put a comment
        review = Review.objects.filter(user=user, product=product).first()

        if review_serializer.is_valid():
            review_serializer.save()
            return Response(review_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)