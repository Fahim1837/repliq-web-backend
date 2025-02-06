from django.db import transaction
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .serializers import LoginSerializer
from .models import User
from apps.helpers.jwt_token import generate_jwt_token


# Create your views here.
class SignupAPIView(GenericAPIView, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):

        with transaction.atomic():
            response = self.create(request, *args, **kwargs)
            user = {
                "user_email": response.data.get("email"),
                "first_name": response.data.get("first_name"),
            }

        return response


class LoginAPIView(GenericAPIView, CreateModelMixin):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token = generate_jwt_token(user)

        return Response(
            {
                "user_id": user.id,
                "refresh_token": token["refresh"],
                "access_token": token["access"],
            }
        )


class LogoutAPIView(GenericAPIView, CreateModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['post']

    def post(self, request):
        return Response({"message": "Logout successful."})
