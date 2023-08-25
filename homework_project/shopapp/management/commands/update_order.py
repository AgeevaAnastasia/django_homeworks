from django.core.management.base import BaseCommand
from shopapp.models import Order


class Command(BaseCommand):
    help = "Update order name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        #parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('АРГУМЕНТ')
        user = Order.objects.filter(pk=pk).first()
        #user.name = name
        order.save()
        self.stdout.write(f'{order}')
