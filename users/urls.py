from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from products.views import FavouriteProductListAPIView, FavouriteProductDestroyAPIView

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view()),
    path('token/', obtain_auth_token),
    path('auth/', include('rest_framework.urls')),

    path('user/<int:pk>/', views.UserRetrieveUpdateAPIView.as_view()),
    path('user/favourite/', FavouriteProductListAPIView.as_view()),
    path('user/favourite/<int:pk>/delete/', FavouriteProductDestroyAPIView.as_view())
]
