import json
from load_django import *
from parser_app.models import *

import requests

cookies = {
    'bse': 'fa8c2b2d192c41698d47db66724d7e85',
    'wdi': '2|E6315A56851F39F4|0x1.9ce1bc02146edp+30|843eecf616f127ec',
    '_ga': 'GA1.2.E6315A56851F39F4',
    'spses.2481': '*',
    'xcj': '1|zcSmX8z2v9zBCFjPI1tCxLjMVLRvtAwaIxVt-qmpQvc',
    'datadome': 'OTw7RI7kl6p7x3J_0GPlVOo0GzIjkufs~sECP1y~oGl3Ptz3ckkOLGWD97lYzYoS0E1UHpxUStSLO2p8fyfS1ZH~dF1rnEmCaUh8CVc9UgZJzUNCisZkjBfteXci4aPp',
    'spid.2481': '64520a4f-39b6-4be8-878c-5d164496ba9c.1731751696.1.1731756301..b0f5d31a-b22b-4879-b3bf-74d0c422782f..a89d4eaa-4add-4943-b258-01dc230f89b7.1731751695705.35',
    '_ga_K9Z2ZEVC8C': 'GS1.2.1731756152.2.1.1731756300.0.0.0',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Nov+16+2024+13%3A25%3A01+GMT%2B0200+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B8%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=1f8794d4-b74f-486b-a469-f61130e59874&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fwww.yelp.de%2Fbiz%2Frausch-schokoladenhaus-berlin-2&groups=BG122%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1',
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
    'x-apollo-operation-name': 'GetRelatedCostGuidesSeparator,GetBizData,GetConsumerFooterCopyrightData',
}

json_data = [
    {
        'operationName': 'GetExtraHeadTagsBizDetails',
        'variables': {
            'BizEncId': 'MqiobbxpvGTciQk75G9u2w',
            'RequestUrl': 'https://www.yelp.de/biz/rausch-schokoladenhaus-berlin-2',
            'ReviewEncId': '',
            'ReviewIsSelected': False,
        },
        'extensions': {
            'operationType': 'query',
            'documentId': 'd71d5fd44e5a5d0b3610cbe12c3b7d84e007acbd437914f5c03055674aa0331b',
        },
    },
]
items = Business.objects.filter(status='DoneReview').order_by('id')
print(len(items))
for business in items:
    json_data[0]['variables']['BizEncId'] = business.business_id
    response = requests.post('https://www.yelp.de/gql/batch', cookies=cookies, headers=headers, json=json_data)
    
    data = response.json()[0]['data']['business']
    
    business.json_data_description = json.dumps(data)
    business.status = 'DoneDescription'
    print('description done')
    business.save()