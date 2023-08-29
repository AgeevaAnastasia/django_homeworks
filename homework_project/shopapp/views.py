from datetime import datetime, timedelta

from django.shortcuts import render
from .models import User, Product, Order


def get_orders(request, customer_id):
    orders = Order.objects.filter(customer__pk=customer_id)
    context = {
        'orders': orders,
        'products': list(Order.objects.filter(products__name="name"))
    }
    return render(request, 'shopapp/orders_customer.html', context)


def get_order(request, order_id):
    order = Order.objects.filter(pk=order_id).first
    prod_list = []
    for prod in Order.objects.filter(products__name="name"):
        prod_list.append(prod)
    context = {'order': order, 'products': prod_list}
    return render(request, 'shopapp/order.html', context)


def get_products_by_user_id(request, user_id: int, period: str):
    user = User.objects.filter(pk=user_id).first()
    current_time = datetime.now()
    if period.lower() == 'week':
        time_filter = current_time - timedelta(weeks=1)
    elif period.lower() == 'month':
        time_filter = current_time - timedelta(days=30)
    elif period.lower() == 'year':
        time_filter = current_time - timedelta(days=365)
    else:
        time_filter = current_time - timedelta(days=365*100)

    # заказы клиента с датой создания >= условной даты
    orders = Order.objects.filter(customer=user, date_ordered__gte=time_filter)
    products = []
    for order in orders:
        products.extend(Order.objects.get(id=order.id).products.all())

    context = {
        'user': user,
        'products': set(products),
    }
    return render(request, "shopapp/user_products.html", context)
