from django.core.management import BaseCommand
from shopapp.models import User, Product, Order


class Command(BaseCommand):
    help = 'get orders by user id'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='user_id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('user_id')
        user = User.objects.filter(pk=pk).first()
        if user:
            orders = Order.objects.filter(customer=user)
            self.stdout.write(f'All orders of customer {user.name} {user.lastname}\n')
            for order in orders:
                self.stdout.write(f'Order from date {order.date_ordered}:'
                                  f'\nTotal price: {order.total_price}')
