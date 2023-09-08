from random import choice, randint


# tmp_address = str(randint(100, 10000)) + ', ' + choice(['Tibbs', 'Ryder', 'Green Gate', 'Lucky Duck', 'Hudson', 'Jenna', 'Snyder', 'Riverwood', 'Trymore', 'Owen', 'Goff', 'Jacobs', 'Barrington', 'Heather Sees', 'University', 'Doe Meadow', 'Kemper', 'Mapleview', 'Gorby', 'Kooter']) + ' ' + choice(['Avenue', 'Lane', 'Drive', 'Street', 'Road', 'Court', 'Way', 'Alley']) + ', ' + choice(['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'])


def handle():
    names = [
        'John', 'Anna', 'Ruth', 'Alice', 'Dan', 'Ethan', 'Eric', 'Sophia', 'Arny', 'Helen',
        'Jane', 'Jude', 'Rina', 'Dana', 'Nina', 'Erin', 'Jack', 'Phil', 'Penn', 'Dennis'
    ]
    lastnames = [
        'Beverly', 'Collins', 'Daniels', 'Davis', 'Miller', 'Taylor', 'Martin', 'Lee', 'Evans',
        'Ford', 'Gilmore', 'Harris', 'Holmes', 'Lambert', 'Moore', 'Newman', 'Riley',
        'Stephenson', 'Wallace', 'Washington'
    ]
    for _ in range(1, 10):
        tmp_name = names[randint(0, 19)]
        tmp_lastname = lastnames[randint(0, 19)]
        tmp_date = (choice(["2020", "2021", "2023"]) + "-"
                    + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                              "11", "12"]) + "-"
                    + choice(["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                              "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                              "21", "22", "23", "24", "25", "26", "27", "28"]))
"""        tmp_address = str(randint(100, 10000)) + ', ' \
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
        tmp_phone = '+1' + ''.join(choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']) for _ in range(10))

        print(
            f'name: {tmp_name}, last name: {tmp_lastname} email: {tmp_name.lower()}{tmp_lastname.lower()}@yahoo.com, phone: {tmp_phone}, address: {tmp_address}, registration: {tmp_date}')

handle()"""

