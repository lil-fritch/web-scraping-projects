'''
Collects links to ads from rental pages with a price filter
'''

import requests
from bs4 import BeautifulSoup
from concurrent import futures

from load_django import *
from app.models import *

DOMAIN = 'https://www.myproperty.ph'

cookies = {
    'userLanguage': 'en',
    'eid': 'mp_1813975939217314',
    'PHPSESSID_lamudi': '1f2e65d007ce29ddde7a4b0ef69ac1c3',
    'device_view': 'full',
    'feature_flags': 'VariableControl%3A1',
    'feature_sets': 'Control',
    'initial_referer': 'https://www.myproperty.ph/',
    '__stp': 'eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiJjNWQyOTNlNi01NjIzLTQwYWQtYmRmOS03ZDU3MmVmODFkZDUifQ==',
    '__stgeo': 'IjAi',
    '__stbpnenable': 'MA==',
    '__stdf': 'MA==',
    '_ga': 'GA1.2.136391095.1729942277',
    '_gid': 'GA1.2.923628422.1729942277',
    'last_prefetch_time': '1729943973',
    'SaveSearchIDs': '[object Object]',
    '__sts': 'eyJzaWQiOjE3Mjk5NDIyNzMxNTAsInR4IjoxNzI5OTQ0MDE1MzI0LCJ1cmwiOiJodHRwcyUzQSUyRiUyRnd3dy5teXByb3BlcnR5LnBoJTJGYnV5JTJGbWV0cm8tbWFuaWxhJTJGcGFzaWclMkYzLWJlZHJvb20tdW5pdC1mb3Itc2FsZS1pbi10aGUtdmFudGFnZS1ieS1yb2Nrd2VsbC0xNzA5MTIyNDI1MTAlMkYiLCJwZXQiOjE3Mjk5NDQwMTUzMjQsInNldCI6MTcyOTk0MjI3MzE1MCwicFVybCI6Imh0dHBzJTNBJTJGJTJGd3d3Lm15cHJvcGVydHkucGglMkZidXklMkZtZXRyby1tYW5pbGElMkZwYXNpZyUyRiIsInBQZXQiOjE3Mjk5NDQwMTAyNTcsInBUeCI6MTcyOTk0NDAxMDI1N30=',
    '_ga_4XWLE7X4RE': 'GS1.2.1729942277.1.1.1729944026.9.0.340280056',
    'clickCount': '3',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.myproperty.ph/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

def main(price_range):
    
        price1, price2 = price_range
        
        for page in range(1, 51):
            
            if page == 50:
                with open('last_page.txt', 'a') as file:
                    file.write(f'{str(price1)}:{str(price2)}\n')
                        
            print('Page:', page, 'Price:', price1, price2)
            
            url = f'https://www.myproperty.ph/buy/?price={price1}-{price2}&page={page}'
            response = requests.get(url)
            
            if response.status_code == 200:
                if 'Real Estate Properties For Sale in the Philippines' in response.text:
                    break
                
                soup = BeautifulSoup(response.text, 'html.parser')
                
                element_with_links = soup.find_all('a', class_='ListingCell-moreInfo-button-v2_redesign')

                links = [link['href'] for link in element_with_links]
                
                for link in links:
                    if link == 'javascript:void(0);': continue
                    item, created = Page.objects.get_or_create(
                        link=link
                    )
                    print(created, item)   
            else:
                print('Error:', response.status_code)
                break

price_ranges = [(price1, price1 + 100000) for price1 in range(100000000, 1000000000, 100000)]

with futures.ThreadPoolExecutor(15) as executor:
    executor.map(main, price_ranges)