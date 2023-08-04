from django.db import models

from users.models import User


# creating a directory for all the product images
def product_image_folder(instance, filename):
    return f'products/{instance.product.serial_number}/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    serial_number = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=None, null=True, blank=True)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_image_folder)


class FavouriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourite_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favourite_products')
