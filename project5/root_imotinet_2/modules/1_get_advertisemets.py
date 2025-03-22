'''
Goes through the saved categories and collects links to ads
'''

import requests
from bs4 import BeautifulSoup
from concurrent import futures

from load_django import *
from app.models import *

URL = 'https://www.imoti.net'

def main(category):
    # for category in categories:
        
    for page in range(1, 100000):
        
        url = category.url.replace('?sid=', f'?page={page}&sid=')
        print(f'Category: {category.name} - Page: {page}')
        
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            all_ads = soup.find_all('a', class_='box-link')
            if len(all_ads) == 0:
                break
            
            for ad in all_ads:
                url = URL + ad['href']
                
                item, created = Advertisement.objects.get_or_create(url=url)
                print(f'{created} - {item}')
        else:
            print('Error:', response.status_code)
                            
    category.status = 'Done'
    category.save()

categories = Category.objects.filter(status='New')
with futures.ThreadPoolExecutor(15) as executor:
    executor.map(main, categories)