from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAdminUser
from .serializers import BooksSerializer, BooksCategorySerializer
from .models import Book, BookCategory


# Create your views here.
class BooksAPIView(
    GenericAPIView,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated(), IsAdminUser()]

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        response.data["message"] = "Books created successfully."
        return response

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        response.data["message"] = "Book updated fully."
        return response

    def patch(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        response.data["message"] = "Book updated partially."
        return response

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response({"message": "Book deleted successfully."})

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            response = self.retrieve(request, *args, **kwargs)
            response.data["message"] = "Book retrieved."
            return response

        # Book List recieved
        return self.list(request, *args, **kwargs)


class BooksCategoryAPIView(
    GenericAPIView,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
):
    serializer_class = BooksCategorySerializer
    queryset = BookCategory.objects.all()
    lookup_field = "id"

    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated(), IsAdminUser()]

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        response.data["message"] = "Book Category created successfully."
        return response

    def put(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        response.data["message"] = "Book Category updated fully."
        return response

    def patch(self, request, *args, **kwargs):
        response = self.update(request, *args, **kwargs)
        response.data["message"] = "Book Category updated partially."
        return response

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response({"message": "Book Category deleted successfully."})

    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            response = self.retrieve(request, *args, **kwargs)
            response.data["message"] = "Book Category retrieved."
            return response

        # Book Category List recieved
        return self.list(request, *args, **kwargs)
