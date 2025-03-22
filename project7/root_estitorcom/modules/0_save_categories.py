'''
Save categories to database
'''
from load_django import *
from parser_app.models import Category

categories = {
    'Prodaja': 'https://estitor.com/me/nekretnine/namjena-prodaja',
    'Izdavanje': 'https://estitor.com/me/nekretnine/namjena-izdavanje',
    'Stan na dan': 'https://estitor.com/me/nekretnine/namjena-stan-na-dan'
}

for category_name, category_url in categories.items():
    item, created = Category.objects.get_or_create(
        name=category_name, 
        url=category_url
    )
    print(f'Category {item.name} created: {created}')