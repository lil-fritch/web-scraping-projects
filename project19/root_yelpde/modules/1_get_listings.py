'''
Collects IDs of businesses
'''

from concurrent import futures
import json
from time import sleep
from bs4 import BeautifulSoup
import requests

from load_django import *
from parser_app.models import *


cookies = {
    'bse': 'c7be5035a44447bc9c2e60029a1302bf',
    'wdi': '2|C94BE7CB0F3DC35C|0x1.9cf995f7bd096p+30|842621c26b6e7d7f',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Nov+21+2024+00%3A41%3A10+GMT%2B0200+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B8%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=85f3abc0-e6ba-4bb2-bb49-213ecab6e91d&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.yelp.de%2Fsearch%3Ffind_loc%3DBerlin&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0',
    'xcj': '1|BIALmwrkbjaLhyg2_AkgUsrbOt4AirVdtkuj3a1kkj4',
    'datadome': '4nEfRdmYmCk9jTokeFTwj5D_0lYz5oD7GdcOyEI4LncYXYH8o_mGleRntHuvjp9B~pV5gceJzWtIB~rDg6hTqnH~~AOuXr631NBuAfHEEQ2Bcjbvd2xfbCiS3AfS0INB',
}

headers = {
    'accept': '*/*',
    'accept-language': 'uk-UA,uk;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.yelp.de',
    'priority': 'u=1, i',
    'referer': 'https://www.yelp.de/search?find_loc=Berlin',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-apollo-operation-name': 'GetBizData,GetConsumerFooterCopyrightData',
}

# URL and payload
url = "https://www.yelp.de/search/snippet"

payload = {
    "find_desc": None,
    "find_loc": None,
    # "cflt": None,
    "start": None,
    "parent_request_id": "309bfb222697edc4",
    "request_origin": "user"
}

proxies={
        "http": "http://rgjbrtfk-rotate:bvltatsjhych@p.webshare.io:80/",
        "https": "http://rgjbrtfk-rotate:bvltatsjhych@p.webshare.io:80/"
    }

results_per_page = 10

# for search in SearchWitoutCategory.objects.filter(status='New').order_by('id'):
def main(search):
    desc = search.decs
    postal_code = search.postal_code
    # cflt = search.category
    
    payload['find_desc'] = desc
    payload['find_loc'] = "Germany+" + postal_code
    # payload['cflt'] = cflt
    
    for i in range(0, 300, results_per_page):
    
        payload['start'] = i
        print(f"Processing {desc}, {postal_code},{i}")
        sleep(0.4)
        response = requests.get(url, headers=headers, params=payload, cookies=cookies) 
    
        if response.status_code == 200:
            try:
                json_data = response.json()
            except json.JSONDecodeError:
                print("Failed to decode JSON")
                
            try:
                data_list = json_data['searchPageProps']['mainContentComponentsListProps'][2:]
            except KeyError:
                break
            
            ids = 0
            count = 0
            for data in data_list:
                bizId = data.get('bizId', None)
                if not bizId:
                    continue
                snippet = data.get('snippet', None)
                if snippet:
                    # description = snippet['text']
                    read_more_url = 'https://www.yelp.de' + snippet['readMoreUrl']
                else:
                    description = None
                    read_more_url = None
                business_url = data.get('searchResultBusiness', None)
                if business_url:
                    business_url = 'https://www.yelp.de/' + business_url['businessUrl']
                
                item, created = Business.objects.get_or_create(
                    business_id=bizId
                )
                item.business_type = desc
                # item.description = description
                item.read_more_url = read_more_url
                item.business_url = business_url
                item.json_data_search = json.dumps(data)
                item.save()
                print(created, item)
                ids += 1
                if not created:
                    count += 1
            if count == 10 and i < 20:
                print("No new data")
                break
            if ids < results_per_page:
                print("No more data")
                break
            search.status = 'Done'
            search.save()
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            break
    
with futures.ThreadPoolExecutor(5) as executor:
    executor.map(main, SearchWitoutCategory.objects.filter(status='Done').order_by('id'))