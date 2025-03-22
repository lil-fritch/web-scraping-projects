'''
Saves categories to database for further processing
'''

from load_django import *
from app.models import *

categories = {
    'Продава': 'https://www.imoti.net/bg/obiavi/r/prodava/?sid=h293VO',
    'Дава под наем': 'https://www.imoti.net/bg/obiavi/r/dava-pod-naem/?sid=iIPrWf',
    'Нощувки': 'https://www.imoti.net/bg/obiavi/r/noshtuvka/?sid=g4IYht',
    'Тьргове': 'https://www.imoti.net/bg/obiavi/r/targove/?sid=jwwiOC',
    'Купува': 'https://www.imoti.net/bg/obiavi/r/kupuva/?sid=eWdgFa',
    'Заменя': 'https://www.imoti.net/bg/obiavi/r/zamenia/?sid=hfs6Rr',
    'Търси да наеме': 'https://www.imoti.net/bg/obiavi/r/tarsi-da-naeme/?sid=e6q4ZG'
}

for category_name, category_url in categories.items():
    item, created = Category.objects.get_or_create(name=category_name, url=category_url)
    print(f'Category {item.name} created: {created}')