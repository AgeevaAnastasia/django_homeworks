from django.urls import path
from .views import index, get_orders, get_order, get_products_by_user_id, all_products, change_product

urlpatterns = [
    path('', index, name='index'),
    path('orders/<int:customer_id>/', get_orders, name='get_orders'),
    path('order/<int:order_id>/', get_order, name='order'),
    path('get_products/<int:user_id>/<str:period>/', get_products_by_user_id),
    path('all_products/', all_products, name='all_products'),
    path('change_product/<int:product_id>/', change_product, name='change_product'),
]