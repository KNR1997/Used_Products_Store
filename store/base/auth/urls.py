from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import ( TokenRefreshView)
from .views import UserRegistrationView
from .views import getAddressByUserId

urlpatterns = [ 
    path('', views.getRoutes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', UserRegistrationView.as_view(), name='user-registration'),

    path('getAllProducts/', views.getAllProducts),
    path('getProduct/<int:id>', views.getProduct),

    path('save-user-address/<int:user_id>', views.saveUserAddress, name='save_user_address'),
    path('get-address/<int:user_id>', views.getAddressByUserId, name='get_address_by_user_id'),

    path('save-order', views.saveOrder, name='save_order'),
    path('getUserOrders/<int:user_id>', views.getUserOrders, name='get_User_Orders'),

    path('save-review', views.saveReview, name='save_review'),
    path('delete-review/<int:review_id>', views.deleteReview, name='delete_review'),

    path('getProductsByUserId/<int:user_id>', views.getProductsByUserId),
]