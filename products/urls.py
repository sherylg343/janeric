from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('product_families/', views.product_families, name='product_families'),
    path('add_pf/', views.add_product_family, name="add_product_family"),
    path('edit_pf/<int:product_family_id>/', views.edit_product_family, name="edit_product_family"),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
