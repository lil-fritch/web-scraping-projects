'''
Walks in steps by latitude and longitude through the states of Australia 
and collects information about agents from the API
'''

import json
import requests

from load_django import *
from parser_app.models import *

url = "https://apps.cpaaustralia.com.au/callaction/"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "referer": "https://apps.cpaaustralia.com.au/find-a-cpa/",
    "traceparent": "00-10c0cfbf27344d048b7e825429ddc4e6-041ad1d10e454895-01",
}

states = {
    # Australia
    'Victoria': {
        'start_x': -34.0,
        'start_y': 150.0,
        'end_x': -40.0,
        'end_y': 140.0
    },
    'New South Wales': {
        'start_x': -28.0,
        'start_y': 153.5,
        'end_x': -37.5,
        'end_y': 150.0
    },
    'Queensland': {
        'start_x': -10.0,
        'start_y': 153.5,
        'end_x': -29.0,
        'end_y': 138.0
    },
    'South Australia': {
        'start_x': -26.0,
        'start_y': 140.0,
        'end_x': -37.0,
        'end_y': 129.0
    },
    'Western Australia': {
        'start_x': -10.0,
        'start_y': 129.0,
        'end_x': -35.0,
        'end_y': 115.0
    },
    'Tasmania': {
        'start_x': -39.0,
        'start_y': 148.0,
        'end_x': -43.5,
        'end_y': 144.0
    },
    'Northern Territory': {
        'start_x': -9.0,
        'start_y': 140.0,
        'end_x': -26.0,
        'end_y': 129.0
    },
    'Australian Capital Territory': {
        'start_x': -35.0,
        'start_y': 149.5,
        'end_x': -35.5,
        'end_y': 149.0
    },
    
    # New Zealand
    'Northland': {
        'start_x': -34.1,
        'start_y': 173.3,
        'end_x': -36.0,
        'end_y': 172.0
    },
    'Auckland': {
        'start_x': -36.0,
        'start_y': 175.0,
        'end_x': -37.3,
        'end_y': 174.2
    },
    'Waikato': {
        'start_x': -37.3,
        'start_y': 176.0,
        'end_x': -38.6,
        'end_y': 174.5
    },
    'Bay of Plenty': {
        'start_x': -37.5,
        'start_y': 177.3,
        'end_x': -38.4,
        'end_y': 175.9
    },
    'Gisborne': {
        'start_x': -37.6,
        'start_y': 178.6,
        'end_x': -38.7,
        'end_y': 177.7
    },
    "Hawke's Bay": {
        'start_x': -38.7,
        'start_y': 178.5,
        'end_x': -40.2,
        'end_y': 176.7
    },
    'Taranaki': {
        'start_x': -38.6,
        'start_y': 174.7,
        'end_x': -39.5,
        'end_y': 173.9
    },
    'Manawatu-Wanganui': {
        'start_x': -39.5,
        'start_y': 176.0,
        'end_x': -40.7,
        'end_y': 174.5
    },
    'Wellington': {
        'start_x': -40.7,
        'start_y': 175.5,
        'end_x': -41.4,
        'end_y': 174.5
    },
    'Tasman': {
        'start_x': -40.5,
        'start_y': 173.6,
        'end_x': -42.0,
        'end_y': 172.7
    },
    'Nelson': {
        'start_x': -41.2,
        'start_y': 173.4,
        'end_x': -41.3,
        'end_y': 173.2
    },
    'Marlborough': {
        'start_x': -40.6,
        'start_y': 174.5,
        'end_x': -41.8,
        'end_y': 173.7
    },
    'West Coast': {
        'start_x': -41.3,
        'start_y': 171.0,
        'end_x': -43.6,
        'end_y': 168.0
    },
    'Canterbury': {
        'start_x': -42.0,
        'start_y': 173.7,
        'end_x': -44.1,
        'end_y': 170.0
    },
    'Otago': {
        'start_x': -44.1,
        'start_y': 170.7,
        'end_x': -46.0,
        'end_y': 168.8
    },
    'Southland': {
        'start_x': -45.8,
        'start_y': 168.6,
        'end_x': -46.7,
        'end_y': 166.4
    }
}

step_x = -0.5
step_y = -0.5

for state, data in states.items():
    print(f"Processing state: {state}")
    
    start_x = data['start_x']
    start_y = data['start_y']
    end_x = data['end_x']
    end_y = data['end_y']
    
    for i in range(10000):
        
        upper_longitude = start_y + i * step_y
        lower_longitude = round(upper_longitude + step_y, 2)
        
        for j in range(100000):
            
            upper_latitude = start_x + j * step_x
            lower_latitude = round(upper_latitude + step_x, 2)
            
            params = {
                "actionName": "cpa_findacpa",
                "parameters": f'{{"EndpointName":"findacpa","UpperLatitude":{upper_latitude},"LowerLatitude":{lower_latitude},"UpperLongitude":{upper_longitude},"LowerLongitude":{lower_longitude}}}'
            }
            response = requests.get(url, headers=headers, params=params)
            print(f"Results for UpperLatitude: {upper_latitude}, LowerLatitude: {lower_latitude}, UpperLongitude: {upper_longitude}, LowerLongitude: {lower_longitude}")
            
            if response.status_code == 200:
                try:
                    all_json_data = response.json() if isinstance(response.json(), list) else json.loads(response.json())
                    
                    for data in all_json_data:
                        
                        account_id = data['accountid']
                        json_data = json.dumps(data)
                        
                        agent, created = Agent.objects.get_or_create(
                            account_id=account_id, 
                            country = ['Australia', 'New Zealand'][upper_longitude > 160],
                            state = state,
                            json_data = json_data
                        )
                        print(created, agent)
                    print('Found:', len(all_json_data))
                    
                except ValueError:
                    print("Failed to parse JSON. Raw response text:", response.text)
            else:
                print("Request failed with status code:", response.status_code)
                print("Response:", response.text)
            
            if upper_latitude < end_x:
                break
                        
        if upper_longitude < end_y:
            break