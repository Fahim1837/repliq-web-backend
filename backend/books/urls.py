from .views import BooksAPIView
from .views import BooksCategoryAPIView
from django.urls import path

# URL configuration for books app.
urlpatterns = [
    path('', BooksAPIView.as_view(), name='books'),
    path('<uuid:id>/', BooksAPIView.as_view(), name='books'),
    path('books-category/', BooksCategoryAPIView.as_view(), name='books'),
    path('books-category/<uuid:id>/', BooksCategoryAPIView.as_view(), name='books'),
]