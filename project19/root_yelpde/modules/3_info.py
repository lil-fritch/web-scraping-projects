'''
Gets business IDs and collects information about them
'''

import requests
import json

from load_django import *
from parser_app.models import *

# Full headers for the request
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "822",
    "content-type": "application/json",
    "cookie": "wdi=2|BFAE1AF9BEF2AFD8|0x1.9cb7cd3b380ep+30|a0ec1e7cdfc3fda7; bse=822421223beb4dc89c5997c36068c388; _ga=GA1.2.BFAE1AF9BEF2AFD8; hl=de_DE; spses.2481=*; bsi=1%7C3f4e1254-4182-5fda-9284-5948f9e37087%7C1731081047321%7C1731080966841%7C2%7C2936948a58dec9fa; xcj=1|LwWMcA8f_tI8eIBzS8Oln893YWPX2rnArd8G_lbJuiQ; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Nov+08+2024+17%3A51%3A10+GMT%2B0200+(Eastern+European+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=1468faff-969d-4409-b5b5-f875b4ac7e6d&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fwww.yelp.de%2Fbiz%2Fvolver-berlin%3Fosq%3DRestaurants&groups=BG122%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1; spid.2481=64a4db09-c160-45a7-ae0b-972b5129722c.1731065149.2.1731081070.1731073864.b353cfc2-3a3a-4fd7-adcb-57b4d1076e4a.2779d8b8-a0b6-437f-85b3-ff294516f336.41688273-fd6b-4c4b-8f82-3ca71eb0243c.1731080968707.13; _ga_K9Z2ZEVC8C=GS1.2.1731080968.4.1.1731081070.0.0.0; datadome=XvXlz1yNXFQN4xPBeVNfy4uUczzodCp1fTLRsaxA9H7pfECHpNA8bXiFfyBdt_Tium2b~Rde5Q1I9rjv2cNPlrJdufmRmfx9D~BeJ5NxmMWVeJB2mz1EHndo5YkzEJrm",
    "origin": "https://www.yelp.de",
    "priority": "u=1, i",
    "referer": "https://www.yelp.de/biz/volver-berlin?osq=Restaurants",
    "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-apollo-operation-name": "GetConsumerFooterCopyrightData,getPushSubscriptionConfig,GetLocalBusinessJsonLinkedData"
}

# Full payload for the request
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

# Sending the POST request
for business in Business.objects.filter(status='Done').order_by('id'):
    if not business.json_data:
        continue
    
    data = json.loads(business.json_data)['business']
    try:
        business.name = data['name']
    except TypeError:
        business.status = 'New'
        business.save()
        continue
    business.phone_number = data['phoneNumber']['formatted']
    if not business.phone_number:
        business.phone_number = None
        
    business.rating = data['rating']
    business.website = data['externalResources']['website']
    if business.website:
        business.website = business.website['url']
    
    location = data['location']['address']
    business.address_line_1 = location['addressLine1']
    if not business.address_line_1:
        business.address_line_1 = None
    business.address_line_2 = location['addressLine2']
    if not business.address_line_2:
        business.address_line_2 = None
    business.address_line_3 = location['addressLine3']
    if not business.address_line_3:
        business.address_line_3 = None
    business.city = location['city']
    business.postal_code = location['postalCode']
    
    business.photo_url = data['primaryPhoto']
    if business.photo_url:
        business.photo_url = business.photo_url['photoUrl']['url']
    
    categories = []
    for category in data['categories']:
        categories.append(category['title'])
    business.categories = categories
    
    business.currency_code = data['currencyCode']
    business.yelp_menu = data['yelpMenu']
    if business.yelp_menu:
        business.yelp_menu = business.yelp_menu['url']
        print(business.name, business.yelp_menu, business.business_id)
        
    operation_hours_data = data['operationHours']
    if operation_hours_data:
        operation_hours_data = operation_hours_data['regularHoursMergedWithSpecialHoursForCurrentWeek']
        operation_hours = {}
        for day in operation_hours_data:
            operation_hours[day['dayOfWeekShort']] = day['hours'][0]
        business.operation_hours = operation_hours
    
    media = data['media']
    photos = []
    if media:
        photos = []
        for photo_data in media['orderedMediaItems']['edges']:
            photo = 'https://s3-media0.fl.yelpcdn.com/bphoto/'+photo_data['node']['encid'] +'/o.jpg'
            photos.append(photo)
    business.photos = photos
    business.review_count = data['reviewCount']        
    business.chain_biz_info = data['chainBizInfo']
    if business.chain_biz_info:
        business.chain_biz_info = business.chain_biz_info['name']
    
    
    business.status = 'Full'
    print(business,'Fulled')
    business.save()
    
    # print(business,'Done', business.review_сount) 
    