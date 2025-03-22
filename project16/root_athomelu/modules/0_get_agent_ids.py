'''
Gets the list of agents' IDs from the api
'''

import json
import requests

from load_django import *
from parser_app.models import Agent

cookies = {
    '_gid': 'GA1.2.369997564.1730960261',
    'intercom-id-bkh4ulpy': '0dbf2670-4c81-470e-a937-d848491bb220',
    'intercom-session-bkh4ulpy': '',
    'intercom-device-id-bkh4ulpy': 'a6f8463c-2b77-4a8d-9ad6-f2459b260edb',
    'OptanonAlertBoxClosed': '2024-11-07T06:17:56.293Z',
    '_gcl_au': '1.1.882660111.1730960276',
    'permutive-id': '803d2018-0c1c-4488-9cb1-148966c815d7',
    '_ga': 'GA1.2.579926260.1730960261',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Thu+Nov+07+2024+08%3A22%3A51+GMT%2B0200+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B8%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=6.15.0&hosts=&consentId=cc338a3e-e5db-46f6-8dca-22061298d43a&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=%3B',
    'cto_bundle': '42uqil9nbXdVZGlpSW5mZW5UZkttdWpYR0FUdE9JRFRhaSUyRmx3ejRaWWlhV1pUNFh4cFVlblJCaEtVcDVQNjZOd3ByUW0xWWxyOU9kdkpSVFV6JTJGODVFNndnSW43UDlReUZPbG82S0RYcGlKbThlOGhUV1p0Y3pFcHR0Qng0cVNwOEZVRTNSUXFGblZ5YWQwblZtQ0FmeG55UWV0T1pnS3VJeU1VNklOdFVkRFF2dXhkemxSaURtRHp2Q2tIR0d5OW1kSzJMRSUyRlJ3OHlNT3pwJTJCNFUwUDdNanNLcmJUaERuVXdRUm55JTJGRWV2dmM2dG83N3dkWW1ZcFUwZkZHemZXZlhiTEx3eWE4NSUyRm5qU1Z2MFRaWW5jRnglMkJpV3BOdTVrU3FFcHlSdFg3MUZ3akU0QXdHaEozNXJYUUx1QUJCTGQydlNQY2Nm',
    '_gat_UA-92432811-1': '1',
    'not_bounced': '1',
    '_ga_7XWTT00X52': 'GS1.1.1730960261.1.1.1730960866.26.0.730511587',
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
}
hkeys = [
    '7ce76d84', '709f2fbb', 'faee1a4a', 
]

for hkey in hkeys:
    response = requests.get(
        f'https://www.athome.lu/client-agency-directory/api/agents?site=lu_at_home&hkeys={hkey}&page[number]=1&page[size]=2000',
        cookies=cookies,
        headers=headers,
    )
    if response.status_code == 200:
        data = response.json()['items']
        for agent_data in data:
            agent_id = agent_data['id']
            item, created = Agent.objects.get_or_create(agent_id=agent_id)
            print(created, item)    