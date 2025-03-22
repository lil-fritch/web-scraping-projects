
from concurrent import futures
import json
from time import sleep
from bs4 import BeautifulSoup
import requests

from load_django import *
from parser_app.models import *

cookies = {
    'bse': 'e89478bfa971451e826573981f0c723f',
    'wdi': '2|518CC04D3964A8D7|0x1.9cc9ac906903fp+30|d9bd0031aeabe037',
    'spses.2481': '*',
    '_ga': 'GA1.2.518CC04D3964A8D7',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Nov+11+2024+22%3A42%3A36+GMT%2B0200+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B8%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=3573db34-67d3-47bf-a2a8-9e9f1c5a3b50&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.yelp.de%2Fsearch%3Ffind_loc%3DBerlin&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0',
    'spid.2481': '06c9ef3c-892e-40d7-8e24-e3d51714bfb1.1731357748.1.1731357758..91376616-ca47-4944-990f-56c29a3d4937..5cb85bb4-737b-4f58-9272-e25c05dac54f.1731357747694.3',
    '_ga_K9Z2ZEVC8C': 'GS1.2.1731357747.1.0.1731357758.0.0.0',
    'xcj': '1|VE_Hs5pCa1wJHHlc0uA3c_hb7BV6gwXckIBwd6rZG3I',
    'datadome': 'zZp23R3EydblBnECwShULWSX4LtN9x7breF0ChlRIXXp7fEyCPwnN9s4eryBseS53txdMkrVsIgb3VGln5FXigg~q6DGzXIZFz1A~UPCMTu8~c~7wpH8h_hyXWVwmP29',
}

headers = {
    'accept': '*/*',
    'accept-language': 'uk-UA,uk;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.yelp.de',
    'priority': 'u=1, i',
    'referer': 'https://www.yelp.de/search?find_loc=Berlin',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-apollo-operation-name': 'GetBizData,GetConsumerFooterCopyrightData',
}

url = "https://www.yelp.de/search/snippet"

payload = {
    "find_desc": None,
    "find_loc": None,
    "cflt": None,
    "start": None,
    "parent_request_id": "309bfb222697edc4",
    "request_origin": "user"
}

results_per_page = 10
for search in Search.objects.filter(pk=1).order_by('id'):
    desc = search.decs
    postal_code = search.postal_code
    cflt = search.category
    
    payload['find_desc'] = desc
    payload['find_loc'] = "Germany+" + postal_code
    payload['cflt'] = cflt
    
    for i in range(1, 300, results_per_page):
    
        payload['start'] = i
        print(f"Processing {desc}, {postal_code}, {cflt}, {i}")
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
            
            with open(f'data_{i}.json', 'w', encoding='UTF-8') as f:
                json.dump(data_list, f, indent=4)
                
            for data in data_list:
                
                bizId = data.get('bizId', None)
                if not bizId:
                    continue
                snippet = data.get('snippet', None)
                if snippet:
                    description = snippet['text']
                    read_more_url = 'https://www.yelp.de' + snippet['readMoreUrl']
                else:
                    description = None
                    read_more_url = None
                item, created = Business.objects.get_or_create(
                    business_id=bizId
                )
                print(created, item)
                ids += 1
            if ids < results_per_page:
                print("No more data")
                break

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            break
