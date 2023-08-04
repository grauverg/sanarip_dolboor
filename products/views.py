from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response

from . import models
from . import serializers
from .permissions import IsAuthor, IsAdminOrReadOnly, IsAuthorImages


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # user can't create products without logging in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # only admin user can create categories
    permission_classes = [IsAdminOrReadOnly]


class ProductImagesListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
    permission_classes = [IsAuthorImages]


class FavouriteProductCreateAPIView(generics.CreateAPIView):
    queryset = models.FavouriteProduct.objects.all()
    serializer_class = serializers.FavouriteProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class FavouriteProductListAPIView(generics.ListAPIView):
    queryset = models.FavouriteProduct.objects.all()
    serializer_class = serializers.FavouriteProductSerializer
    permission_classes = [IsAuthor, ]

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user.id)  # filtering the queryset for user
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class FavouriteProductDestroyAPIView(generics.DestroyAPIView):
    queryset = models.FavouriteProduct.objects.all()
    serializer_class = serializers.FavouriteProductSerializer
    permission_classes = [IsAuthor, ]
