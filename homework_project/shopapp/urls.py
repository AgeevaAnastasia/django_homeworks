from django.urls import path
from .views import get_orders, get_order, get_products_by_user_id

urlpatterns = [
    path('orders/<int:customer_id>/', get_orders),
    path('order/<int:order_id>/', get_order, name='order'),
    path('get_products/<int:user_id>/<str:period>/', get_products_by_user_id),
]