'''
Collects links to ads from rental pages with a price filter
'''

import requests
from bs4 import BeautifulSoup
from concurrent import futures

from load_django import *
from app.models import *

DOMAIN = 'https://www.lamudi.com.ph'

cookies = {
    'FECW': 'c2d75e53772323919eaa2e46e7007e1faa31492cb1fa2ead75a65fd4469f8bf370e69dadc123ca6558886c83074647bfcbd716cbdb5d5802413977f91d95118d715a66eb59cb74dbfdf436dbadc1ab4785',
    'initial_referer': 'https://www.lamudi.com.ph/',
    'userLanguage': 'en',
    'device_view': 'full',
    '_rtb_user_id': '3659d775-98c3-ebba-dcbb-4926a1f866d3',
    'eid': 'ph_1813699876014220',
    'PHPSESSID_lamudi': 'de871c678149f2573bcd19cb7d02954e',
    'cebs': '1',
    '_ce.clock_event': '1',
    '_ce.clock_data': '622%2C91.218.90.63%2C1%2C16453d6e2683b8800ded2a27c7f595d9%2CChrome%2CUA',
    '_gcl_au': '1.1.2065248222.1729678991',
    '_gid': 'GA1.3.1762007838.1729678991',
    'feature_flags': 'VariableControl%3A1',
    'feature_sets': 'Control',
    'clickCount': '3',
    '_tac': 'false~self|not-available',
    '_ta': 'ph~1~2e455cbbc97dbac763d8b87532c0d44b',
    '_recent_searches': '["/buy/metro-manila/quezon-city/fairview/house/","/buy/"]',
    'reese84': '3:crhO/I0R6jWcGPcm+t0ZNg==:P46X/aRPBjofudsxTUvml9OHcGObCOZwKuBhrA1zHz209w32aLTjwXGdax5ZNXU8bAgVyKh9AmHfZsIsWbOONayqvyQG1GPm7WX7GuOCzLdu0lIh27cCVQ9dw1YJSSlQphAYjKlpYTIMJfxvn8JiGeIgHDe0n+70TzvypsZBXApp6RerrKkhE0D/5lXg0EtuDabXml7sRzSFAZdYfCBsHLKZ5gsmAKxl+kYLEyAsmx4PTrtdmUTld31ezp7qtYLhJIxTmlftFY+5H4dbUnWdQnnuhzS9Vz2QOI5wRz9jqIq2J0JoFv+ge1N0lyqrf2VVBXGqe7yYgAERM9mNokG88zHBq/1IT+Q3ogkoYMSsJ2ypOKEJtogQQ++g82KjPIARynTO2pIOqsPi7RIPfNWtmKr47erk7s8iw09oQj6UlbQ4prxUfj1OJn47JvARTyAOi9WIatKQU4nIazghnkzi+Q==:3JbKT+spDYbJLf2iQpmHC9XNusHsg3PXGUxnTe8cM2o=',
    'sid': 'ph_1813710123796559',
    '_tas': 'dx1vhkkd47',
    'submitLead': '6',
    'last_prefetch_time': '1729689094',
    '_ga_SX0X12TPQ5': 'GS1.1.1729678990.1.1.1729689095.0.0.0',
    'cebsp_': '92',
    '_ga': 'GA1.3.1142403826.1729678990',
    '_dc_gtm_UA-48934674-20': '1',
    'FECA': '06qGqzDS+wV+mBki4g+2RqLx4FyqnpIXaLn5gwFhXDzOXQeeKZ1s3tqVZw5ioOcXZLxo6GJ/qtkm4hnOecuxFTF7WHKxcwhpIJCqBKctDIaNQDcDah+9IjKfSWPYv/HHlVfNfqr/U7BvS+b1YCAqX585O/lByKTiJfDB56h88NoTt/9ThwKLG4klgedpoYSya0',
    '_ga_SXHWQSEZYL': 'GS1.3.1729678991.1.1.1729689095.60.0.0',
    '_ce.s': 'v~e359527a42a1b98820f432ad555b27117860ff77~lcw~1729689096552~vir~new~lva~1729678990471~vpv~0~v11.fhb~1729678990761~v11.lhb~1729689095410~v11.cs~420166~v11.s~548c4cb0-9140-11ef-ab19-ef3da4aefefe~v11.sla~1729689096559~v11.send~1729689096223~lcw~1729689096559',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

def main(price_range):
    
        price1, price2 = price_range
        
        for page in range(1, 51):
            
            print('Page:', page, 'Price:', price1, price2)
            
            url = f'https://www.lamudi.com.ph/buy/?price={price1}-{price2}&page={page}'
            response = requests.get(url)
            
            if response.status_code == 200:
                if '1 Bedroom UGF (City View) Condo Unit for Sale in Davao City, Davao del Sur at Fronter' in response.text:
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

price_ranges = [(price1, price1 + 1000) for price1 in range(1000, 100000000, 1000)]

with futures.ThreadPoolExecutor(20) as executor:
    executor.map(main, price_ranges)