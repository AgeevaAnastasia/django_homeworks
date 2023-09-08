from django.core.management.base import BaseCommand
from shopapp.models import Product, User, Order
from random import randint, choice


class Command(BaseCommand):
    help = "Generate fake orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for _ in range(1, count + 1):
            tmp_prods = []
            tmp_price = 0
            cnt = randint(1, 4)
            for i in range(cnt):
                prod = Product.objects.get(pk=randint(0, 50))
                tmp_prods.append(prod)
                tmp_price += prod.price
            tmp_date = (choice(["2022", "2023"]) + "-"
                        + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                  "11", "12"]) + "-"
                        + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                  "21", "22", "23", "24", "25", "26", "27", "28"]))

            order = Order(customer=User.objects.filter(pk=randint(1, 20)).first(),
                          total_price=tmp_price,
                          date_ordered=f'{tmp_date}')
            order.save()
            order.products.add(*tmp_prods)
            order.save()
        self.stdout.write(f'{count} orders created')


