from django.db import models
from django.db.models.fields import IntegerField


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    division = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_division(self):
        return self.division


class Product_Family(models.Model):
    class Meta:
        verbose_name_plural = 'Product_Families'

    name = models.CharField(max_length=254)
    brand_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_brand_name(self):
        return self.brand_name


class Product(models.Model):
    BOTTLE_SIZES = (
        ('8oz.', "8 oz."),
        ('16oz', "16 oz."),
        ('18oz', "18 oz."),
        ('32oz', "32 oz."),
        ('Gallon', "Gallon"),
    )

    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    product_family = models.ForeignKey(
        "Product_Family", null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    SKU = models.CharField(
        max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    size = models.CharField(
        max_length=254, null=True, blank=True, choices=BOTTLE_SIZES)
    pack = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    description = models.TextField(
        null=True, blank=True)

    def __str__(self):
        return self.name

