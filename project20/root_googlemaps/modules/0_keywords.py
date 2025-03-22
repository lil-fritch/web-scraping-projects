import csv

from load_django import *
from parser_app.models import *

country = 'Australia'
zip_code = None
name = 'accounting+firm'
state = 'VIC'
city = 'Cordova'
category = 'Accounting firm'

def get_victoria_postcodes(file_path):
    victoria_postcodes = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаємо заголовок
        for row in reader:
            if row[2].strip() == 'VIC':
                victoria_postcodes.append(row)
    return victoria_postcodes 

file_path = 'A:\\_job\\project20\\root_googlemaps\\modules\\australian_postcodes.csv'
victoria_zip_codes = get_victoria_postcodes(file_path)

for data in victoria_zip_codes:
    zip_code = data[0]
    city = data[1]
    state = data[2]

    link = f'https://www.google.com.ua/maps/search/{name}+near+{zip_code}+{state}+{country}/?hl=en'

    obj, created = Keyword.objects.get_or_create(

        country = country,
        city = city,
        state = state,
        zip_code = zip_code,

        category = category,
        name = name,
        link = link,
    )
    print(created, obj)