from .views import BooksAPIView
from .views import BooksCategoryAPIView
from django.urls import path

# URL configuration for books app.
urlpatterns = [
    path('books/', BooksAPIView.as_view(), name='books'),
    path('books-category/', BooksCategoryAPIView.as_view(), name='books'),
]