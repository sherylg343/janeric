from django.contrib import admin
from .models import Product, Category, Product_Family


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'SKU',
        'name',
        'product_family',
        'category',
        'image',
        'size',
        'pack',
        'price',
        'description',
    )

    ordering = ('product_family',)


class Product_FamilyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand_name'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'division'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product_Family, Product_FamilyAdmin)
