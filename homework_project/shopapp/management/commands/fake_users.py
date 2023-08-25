from django.core.management.base import BaseCommand
from shopapp.models import User
from random import randint, choice


class Command(BaseCommand):
    help = "Generate fake users"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        names = [
            'John', 'Anna', 'Ruth', 'Alice', 'Dan', 'Ethan', 'Eric', 'Sophia', 'Arny', 'Helen',
            'Jane', 'Jude', 'Rina', 'Dana', 'Nina', 'Erin', 'Jack', 'Phil', 'Penn', 'Dennis'
        ]
        lastnames = [
            'Beverly', 'Collins', 'Daniels', 'Davis', 'Miller', 'Taylor', 'Martin', 'Lee', 'Evans',
            'Ford', 'Gilmore', 'Harris', 'Holmes', 'Lambert', 'Moore', 'Newman', 'Riley',
            'Stephenson', 'Wallace', 'Washington'
        ]
        count = kwargs.get('count')
        for _ in range(1, count + 1):
            tmp_name = names[randint(0, 19)]
            tmp_lastname = lastnames[randint(0, 19)]
            tmp_date = (choice(["2020", "2021", "2023"]) + "-"
                        + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                  "11", "12"]) + "-"
                        + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                                  "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                                  "21", "22", "23", "24", "25", "26", "27", "28"]))
            tmp_address = str(randint(100, 10000)) + ', ' \
                          + choice(['Tibbs', 'Ryder', 'Green Gate', 'Lucky Duck', 'Hudson',
                                    'Jenna', 'Snyder', 'Riverwood', 'Trymore', 'Owen', 'Goff',
                                    'Jacobs', 'Barrington', 'Heather Sees', 'University',
                                    'Doe Meadow', 'Kemper', 'Mapleview', 'Gorby', 'Kooter']) + ' ' \
                          + choice(['Avenue', 'Lane', 'Drive', 'Street', 'Road', 'Court', 'Way',
                                    'Alley']) + ', ' \
                          + choice(['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
                                    'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
                                    'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana',
                                    'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
                                    'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
                                    'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
                                    'New Jersey', 'New Mexico', 'New York', 'North Carolina',
                                    'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
                                    'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
                                    'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
                                    'West Virginia', 'Wisconsin', 'Wyoming'])

            user = User(name=f'{tmp_name}',
                        lastname=f'{tmp_lastname}',
                        email=f'{tmp_name.lower()}{tmp_lastname.lower()}@yahoo.com',
                        phone='+1'+ ''.join(choice(['1', '2', '3', '4', '5', '6', '7', '8',
                                                   '9', '0']) for _ in range(10)),
                        address=f'{tmp_address}',
                        registration=f'{tmp_date}')
            user.save()
        self.stdout.write(f'{count} users created')
