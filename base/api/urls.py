from django.urls import path
from . import views

urlpatterns = [
    path('books', views.getBooks),
    path('books/<int:id>/', views.getBook),

    path('reviews/search/findByBookId/<int:id>/', views.getReviewsByBookId)
]