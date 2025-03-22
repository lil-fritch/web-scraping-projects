'''
Stores countries for further filtering in the database
'''
from load_django import *
from parser_app.models import *

url = 'https://www.indomio.al/en/agents'

countries = {
    'Albania': 'https://www.indomio.al/en/agents',
    'Greece': 'https://www.indomio.al/en/agents/greece',
    'Bulgaria': 'https://www.indomio.al/en/agents/bulgaria',
    'Serbia': 'https://www.indomio.al/en/agents/serbia',
    'Croatia': 'https://www.indomio.al/en/agents/croatia',
    'Slovenia': 'https://www.indomio.al/en/agents/slovenia',
    'Montenegro': 'https://www.indomio.al/en/agents/montenegro',
    'Bosnia and Herzegovina': 'https://www.indomio.al/en/agents/bosnia-and-herzegovina',
    'Malta': 'https://www.indomio.al/en/agents/malta',
    'Cyprus': 'https://www.indomio.al/en/agents/cyprus-country',
    'Germany': 'https://www.indomio.al/en/agents/germany',
    'Ramaining countries': 'https://www.indomio.al/en/agents/remaining-countries',
    'Austria': 'https://www.indomio.al/en/agents/austria',
    'Italy': 'https://www.indomio.al/en/agents/italy',
    'Turkey': 'https://www.indomio.al/en/agents/turkey',
    'France': 'https://www.indomio.al/en/agents/france',
    'Spain': 'https://www.indomio.al/en/agents/spain',
    'Switzerland': 'https://www.indomio.al/en/agents/switzerland',
    'USA': 'https://www.indomio.al/en/agents/usa',
}

for country_name, country_url in countries.items():
    item, created = Country.objects.get_or_create(name=country_name, url=country_url)
    print(f'Country {item.name} created: {created}')