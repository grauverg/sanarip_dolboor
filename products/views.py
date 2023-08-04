from django.shortcuts import redirect
from django.urls import reverse
from rest_framework import generics, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from . import serializers
from .permissions import IsAuthor, IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # user can't create products without logging in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # @action(
    #     methods=["GET", "POST"],
    #     detail=True,
    #     serializer_class=serializers.FavouriteProductSerializer,
    #     permission_classes=[permissions.IsAuthenticated, ],
    # )
    # def favourite(self, request, pk=None):
    #     if request.method == "GET":
    #         queryset = models.FavouriteProduct.objects.filter(product=self.kwargs['pk'])
    #         serializer = serializers.FavouriteProductSerializer(instance=queryset, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #     if request.method == "POST":
    #         serializer = self.get_serializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save(
    #                 user=self.request.user.profile,
    #                 product=self.get_object()
    #             )
    #             return redirect(reverse(ProductViewSet.as_view()), {'msg': 'successfully'})
    #         return Response(serializer.errors)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # only admin user can create categories
    permission_classes = [IsAdminOrReadOnly]


class ProductImagesListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.ProductImage.objects.all()
    serializer_class = serializers.ProductImageSerializer
    permission_classes = [IsAuthor]


class FavouriteProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.FavouriteProduct.objects.all()
    serializer_class = serializers.FavouriteProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(self.kwargs['product_id'])

        serializer.save(
            user=self.request.user,
            product=generics.get_object_or_404(models.Product, id=self.kwargs['product_id'])
        )
