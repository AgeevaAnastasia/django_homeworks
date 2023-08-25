from django.core.management import BaseCommand
from shopapp.models import User, Order


class Command(BaseCommand):
    help = 'delete orders by user id'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='user_id')

    def handle(self, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = User.objects.filter(pk=user_id).first()
        if user:
            orders = Order.objects.filter(customer=user)
            for order in orders:
                order.delete()
                self.stdout.write(f'order {order} deleted')
