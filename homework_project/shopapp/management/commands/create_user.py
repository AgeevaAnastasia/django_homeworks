from django.core.management import BaseCommand
from shopapp.models import User


class Command(BaseCommand):
    help = 'Create user'

    # передача нескольких параметров в командной строке
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('lastname', type=str, help='User last name')
        parser.add_argument('email', type=str, help='Email')
        parser.add_argument('phone', type=str, help='Phone')
        parser.add_argument('address', type=str, help='Address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        lastname = kwargs.get('lastname')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        user = User(
            name=name,
            lastname=lastname,
            email=email,
            phone=phone,
            address=address
        )
        user.save()
        self.stdout.write(f'User {user} created')
