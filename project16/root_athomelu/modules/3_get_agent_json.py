'''
Gets json for each agent via api
'''

import json
from load_django import *
from parser_app.models import *

import requests

cookies = {
    '_gid': 'GA1.2.369997564.1730960261',
    'intercom-id-bkh4ulpy': '0dbf2670-4c81-470e-a937-d848491bb220',
    'intercom-session-bkh4ulpy': '',
    'intercom-device-id-bkh4ulpy': 'a6f8463c-2b77-4a8d-9ad6-f2459b260edb',
    'OptanonAlertBoxClosed': '2024-11-07T06:17:56.293Z',
    '_gcl_au': '1.1.882660111.1730960276',
    'permutive-id': '803d2018-0c1c-4488-9cb1-148966c815d7',
    'not_bounced': '1',
    'PHPSESSID': 'ci1lg4c0hq8hl9ohkc7h41b6r0',
    '_ga': 'GA1.2.579926260.1730960261',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Thu+Nov+07+2024+13%3A37%3A21+GMT%2B0200+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B8%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=6.15.0&hosts=&consentId=cc338a3e-e5db-46f6-8dca-22061298d43a&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=%3B',
    'cto_bundle': '1GBzp19nbXdVZGlpSW5mZW5UZkttdWpYR0FXbGhLQzJwb0sya0V3R1ZvdTdHTVhaYm82SjlUbGFmS2J4QUtBeFdtdk9GMFVndDglMkZNd01TcDQlMkI2RHVocW1TRDBIUlVIR3pPalpsbXljcXVyVXN1WmhEZ3BmS2ZQc0NYSGlKdVByQjZXRGp6ZSUyQm93Q0lUUFdPZ3VEaTFBeVpJYWZ0NmpXckVRTXNoWFF5UXphJTJCeWhLJTJCRzBvYkl1cHdaJTJCRzg2Q1pXTDZ3JTJCSm5NSGJRWU5yMElhNEZnY011d3lXTzdTdFZWNGE2NVVRQWVoa1dITHJ3eTY5eDdINXNENFBOa0Ezc2Q3cUpGRjVMYmtidWtyUnlCb0xGcjc5VzJaZVZod0hMZVF3TTFiaGZCdG1uVWZWaDJMOWQ1amJ4UUJSc2J6NW9xR0htMjRB',
    '_ga_7XWTT00X52': 'GS1.1.1730979387.2.1.1730979453.60.0.1456517761',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-brand': 'athomelu',
}


for agent in Agent.objects.all():
    if agent.json_data:
        continue 
    response = requests.get(f'https://www.athome.lu/client-agency/api/agents/{agent.agent_id}', cookies=cookies, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        agent.json_data = json.dumps(data)
        agent.save()
        print(agent.agent_id, 'updated')
    else:
        print('Error:', response.status_code)
        