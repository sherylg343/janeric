from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add//', views.add_to_cart, name='add_to_cart'),
    path('adjust/<int:product_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<product_id>/', views.remove_from_cart, name="remove_from_cart"),
]

