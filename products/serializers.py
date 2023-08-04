import rest_framework.serializers as serializers
from django.db import IntegrityError

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'serial_number',
                  'description', 'categories', 'images')


class FavouriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavouriteProduct
        fields = ('id', 'user', 'product')

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            instance = self.Meta.model.objects.get(validated_data)
            instance.delete()
