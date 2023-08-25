from django.core.management import BaseCommand
from shopapp.models import User, Product, Order


class Command(BaseCommand):
    help = 'Create order'

    # передача нескольких параметров в командной строке
    def add_arguments(self, parser):
        parser.add_argument('user', type=int, help='user_id')
        parser.add_argument('product', nargs='*', type=int, help=' one or several product_id')

    def handle(self, *args, **kwargs):
        user_id = kwargs.get('user')
        user = User.objects.filter(pk=user_id).first()
        products = kwargs.get('product')
        total_price = 0
        for item in products:
            product = Product.objects.filter(pk=item).first()
            total_price += product.price
        order = Order(
            customer=user,
            total_price=total_price,
        )
        order.save()
        order.products.add(*products)
        order.save()
        self.stdout.write('order created')
