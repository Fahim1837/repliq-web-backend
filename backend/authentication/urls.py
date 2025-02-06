from django.urls import path
from .views import SignupAPIView
from .views import LoginAPIView
from .views import LogoutAPIView

# URL configuration for authentication apps.
urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name= 'login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]