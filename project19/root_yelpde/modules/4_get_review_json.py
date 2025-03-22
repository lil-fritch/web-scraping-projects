from concurrent import futures
from load_django import *
from parser_app.models import *

import requests
import json

cookies = {
    'bse': 'cde6202ca9504519800b39197beb0c29',
    'wdi': '2|65FB33EF275106F7|0x1.9ce7014bab34ap+30|97fde0b34b9ed9c1',
    'datadome': 'crz4YvYNxRFzmFqHSS~_8KTZjSPRbjjFpS8GMt~dlRLonhoELIskvh~FNp1RHF1e~TrnGNTdgPjrl~2d_mwcdYEyUUJQIWJr5eh6XMBu3Ima4Fiy5K2BzzY8pOYMeqzO',
    'xcj': '1|mqsN5U3j2pKrra2s47Ou0vErXD4qvbacE83CWtPN98k',
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

data = [
    {
        'operationName': 'GetBusinessReviewFeed',
        'variables': {
            'encBizId': None,
            'reviewsPerPage': 49,
            'selectedReviewEncId': '',
            'hasSelectedReview': False,
            'sortBy': 'RELEVANCE_DESC',
            'languageCode': 'de', 
            'ratings': [
                5,
                4,
                3,
                2,
                1,
            ],
            'queryText': '',
            'isSearching': False,
            'after': None,
            'isTranslating': False,
            'translateLanguageCode': 'de',
            'reactionsSourceFlow': 'businessPageReviewSection',
            'guv': '002037FAB3F0FEAB',
            'minConfidenceLevel': 'HIGH_CONFIDENCE',
            'highlightType': '',
            'highlightIdentifier': '',
            'isHighlighting': False,
        },
        'extensions': {
            'operationType': 'query',
            'documentId': 'ebfc1971a31a1f28a9b5e812f760986ab6528d7b813635ca3ac2f31338f74cae',
        },
    },
]

# for business in Business.objects.filter(status='Full').order_by('id')[:50]:
def main(business):
    print(business)
    data[0]['variables']['encBizId'] = business.business_id
    response = requests.post('https://www.yelp.de/gql/batch', cookies=cookies, headers=headers, json=data)
    
    if response.status_code==200:
        
        with open('response.json', 'w') as f:
            json.dump(response.json(), f, indent=4)
        
        json_data = response.json()[0]['data']
        
        review_counts = json_data['business']['reviewCountsByRating']
        business.stars_1 = review_counts[0]
        business.stars_2 = review_counts[1]
        business.stars_3 = review_counts[2]
        business.stars_4 = review_counts[3]
        business.stars_5 = review_counts[4]
        business.save()
        
        reviews_data = json_data['business']['reviews']['edges']
        
        for review_data in reviews_data:
            review_id = review_data['node']['encid']
            review_json = json.dumps(review_data)
            
            item, created = Review.objects.get_or_create(
                business_id=business,
                business_name=business.name, 
                review_id=review_id,
                json_data=review_json,
            )
            
            print(created, item)
        
        business.status =  'DoneReview'
        business.save()
    else:
        print(response.status_code)

objects = Business.objects.filter(status='Full').order_by('id')
with futures.ThreadPoolExecutor(1) as executor:
    executor.map(main, objects)