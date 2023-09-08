from django.core.management.base import BaseCommand
from shopapp.models import Product
from random import randint, choice


class Command(BaseCommand):
    help = "Generate fake products"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        products = [
            'TV', 'coffee maker', 'dishwasher', 'cooker', 'phone', 'electric kettle', 'iron',
            'microwave', 'washing machine', 'oven', 'deep fryer', 'heater', 'coffee grinder',
            'juicer', 'fan', 'humidifier', 'refrigerator', 'mixer', 'stereo system', 'hairdryer',
            'vacuum cleaner', 'dishwasher', 'fridge', 'toaster', 'microwave', 'air conditioner',
            'kitchen combiner', 'blender'
        ]
        descriptions = [
            'best price', 'free shipping', 'free returns', 'money back guarantee', 'advantage',
            'remarkable', 'magnificient', 'wonderful', 'extremely well', 'contemporary', 'powerful',
            'solid', 'practical', 'convenient', 'original', 'automatic', 'complex', 'electric'
        ]
        count = kwargs.get('count')
        for _ in range(1, count + 1):
            tmp_prod = products[randint(0, 19)]
            tmp_date = (choice(["2022", "2023"]) + "-"
                        + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                  "11", "12"]) + "-"
                        + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                  "21", "22", "23", "24", "25", "26", "27", "28"]))

            product = Product(name=f'{tmp_prod}',
                              price=randint(50, 1000),
                              description=', '.join(choice(descriptions) for _ in range(7)),
                              amount=randint(10, 100),
                              add_date=f'{tmp_date}')
            product.save()
        self.stdout.write(f'{count} products created')
