from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import ( TokenRefreshView)
from .views import UserRegistrationView

urlpatterns = [ 
    path('', views.getRoutes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', UserRegistrationView.as_view(), name='user-registration'),

    path('getAllProducts/', views.getAllProducts),
]