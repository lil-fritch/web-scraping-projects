'''
Gets business IDs and collects information about them
'''

from concurrent import futures
import requests
import json

from load_django import *
from parser_app.models import *

payload = [
    {
        "operationName": "GetConsumerFooterCopyrightData",
        "variables": {},
        "extensions": {
            "operationType": "query",
            "documentId": "7afdec92e3e0c56c236ac65165bcf2d8c6bd183b1f232703501e65f295108b7a"
        }
    },
    {
        "operationName": "getPushSubscriptionConfig",
        "variables": {
            "Domain": "WWW",
            "Cohort": "status_quo",
            "SubscriptionUrl": "/browser_push_notifications/subscribe"
        },
        "extensions": {
            "operationType": "query",
            "documentId": "516e39d55bcbf815a7568eaaee05583fb2a18acdfdd87173dcfd1a20e346ad59"
        }
    },
    {
        "operationName": "GetLocalBusinessJsonLinkedData",
        "variables": {
            "encBizId": "0f3-k1Hyu6__ajXjRpDbCg",
            "ChainInfoEnabled": True,
            "FetchVideoMetadata": True,
            "MediaItemsLimit": 25,
            "ReviewsPerPage": 10,
            "HasSelectedReview": False,
            "SelectedReviewEncId": ""
        },
        "extensions": {
            "operationType": "query",
            "documentId": "3cbee7cb76a5f43277374289f3b0df7fe24af3d1e40a66bbf42593ee71b306c3"
        }
    }
]

import requests

cookies = {
    'bse': 'cde6202ca9504519800b39197beb0c29',
    'wdi': '2|65FB33EF275106F7|0x1.9ce7014bab34ap+30|97fde0b34b9ed9c1',
    'xcj': '1|Gb0Z_fk3Dd5H8PYs_VZBm_0xEqeTeOC0Aiy-uDzV3bs',
    'datadome': 'crz4YvYNxRFzmFqHSS~_8KTZjSPRbjjFpS8GMt~dlRLonhoELIskvh~FNp1RHF1e~TrnGNTdgPjrl~2d_mwcdYEyUUJQIWJr5eh6XMBu3Ima4Fiy5K2BzzY8pOYMeqzO',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Nov+17+2024+12%3A09%3A07+GMT%2B0200+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B8%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=3c86ceab-ed1c-413f-9e3d-581ae5693d22&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fwww.yelp.de%2Fsearch%3Ffind_loc%3DBerlin',
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



for business in Business.objects.filter(status='New').order_by('id'):
# def main(business):
    payload[2]['variables']['encBizId'] = business.business_id
    response = requests.post("https://www.yelp.de/gql/batch", headers=headers, json=payload, cookies=cookies)
    if response.status_code == 200:
        with open(f"{business.business_id}.json", 'w') as f:
            json.dump(response.json(), f, indent=4)
        data = response.json()[2]['data']
        business.json_data = json.dumps(data)
        business.status = 'Done'
        business.save()
        print(f"Business {business.business_id} has been updated")  
    else:
        print(f"Error: {response.status_code}")

# objects = Business.objects.filter(status='New').order_by('id')
# with futures.ThreadPoolExecutor(3) as executor:
#     executor.map(main, objects)