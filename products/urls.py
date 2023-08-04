from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('images/', views.ProductImagesListCreateAPIView.as_view()),
    path('product/<int:product_id>/favourite/', views.FavouriteProductListCreateAPIView.as_view()),
]
