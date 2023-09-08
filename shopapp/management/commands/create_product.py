from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    help = 'Create product'

    # передача нескольких параметров в командной строке
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='product_name')
        parser.add_argument('price', type=float, help='price')
        parser.add_argument('description', type=str, help='description')
        parser.add_argument('amount', type=int, help='amount')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        price = kwargs.get('price')
        description = kwargs.get('description')
        amount = kwargs.get('amount')
        product = Product(
            name=name,
            description=description,
            price=price,
            amount=amount,
        )
        product.save()
        self.stdout.write('product created')
