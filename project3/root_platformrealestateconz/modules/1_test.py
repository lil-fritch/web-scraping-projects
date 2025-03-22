import requests
import json
import time

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

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
    params = {'filter[q]': letter, 'page[offset]': 0, 'page[limit]': 100}
    offset = 0

    while True:
        print(f"Letter: {letter}, Offset: {offset}")
        params['page[offset]'] = offset
        response = requests.get('https://platform.realestate.co.nz/search/v1/agents', headers=headers, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            break

        agent_data = response.json().get('data', [])
        if not agent_data:
            break

        for agent in agent_data:
            agent_id = agent['id']
            agent_json = json.dumps(agent)

            item, created = Agent.objects.get_or_create(
                agent_id=agent_id, defaults={'json_data': agent_json}
            )
            print(item, created)

        offset += len(agent_data)
        if len(agent_data) < 100:  # Якщо менше записів, ніж ліміт — вихід
            break
