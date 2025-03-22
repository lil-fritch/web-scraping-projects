import requests
import json

from load_django import *
from app.models import Agent

headers = {
    "authority": "platform.realestate.co.nz",
    "method": "GET",
    "scheme": "https",
    "accept": "application/vnd.api+json",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://www.realestate.co.nz",
    "referer": "https://www.realestate.co.nz/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

params = {
    'filter[q]': 'a',
    'page[offset]': 0,
    'page[limit]': 1000 
}

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter1 in alp:
    for letter2 in alp:
        params['filter[q]'] = f'{letter1}{letter2}'
        offset = 0

        while True:
            print(f"Letter: {letter1}{letter2}, Offset: {offset}")
            params['page[offset]'] = offset
            response = requests.get(
                'https://platform.realestate.co.nz/search/v1/agents', 
                headers=headers, 
                params=params
            )

            if response.status_code != 200:
                print(f"Error: {response.status_code}")
                break

            json_data = response.json()
            agent_data = json_data.get('data', [])

            if not agent_data:
                break

            for agent in agent_data:
                agent_id = agent['id']
                json_data = json.dumps(agent)
                try:
                    item, created = Agent.objects.get_or_create(
                        agent_id=agent_id, 
                        json_data=json_data
                    )
                    print(item, created)
                except Exception as e:
                    with open('errors.txt', 'a', encoding='UTF-8') as f:
                        print(e)
                        f.write(f'{e}\n{agent_id}\n{json_data}\n\n')

            offset += len(agent_data)