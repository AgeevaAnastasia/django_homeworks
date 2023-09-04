from datetime import datetime, timedelta

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import User, Product, Order
from .forms import ProductForm


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


def all_products(request):
    products = Product.objects.all()
    return render(request, 'shopapp/products.html', {'products': products})


def change_product(request, product_id):
    message = ''
    product = Product.objects.filter(pk=product_id).first()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            if isinstance(image, bool):
                image = None
            if image is not None:
                fs = FileSystemStorage()
                fs.save(image.name, image)
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.amount = form.cleaned_data['amount']
            product.add_date = form.cleaned_data['add_date']
            product.image = image
            product.save()
            message = f'Product {product.name} was changed'

        return all_products(request)

    else:
        form = ProductForm(initial={'name': product.name,
                                    'price': product.price,
                                    'description': product.description,
                                    'amount': product.amount,
                                    'add_date': product.add_date,
                                    'image': product.image})

    return render(request, 'shopapp/change_product.html', {'form': form, 'message': message})
