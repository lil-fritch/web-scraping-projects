from concurrent import futures
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
    'PHPSESSID': 'ci1lg4c0hq8hl9ohkc7h41b6r0',
    '_ga': 'GA1.2.579926260.1730960261',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Thu+Nov+07+2024+18%3A07%3A14+GMT%2B0200+(%D0%B7%D0%B0+%D1%81%D1%85%D1%96%D0%B4%D0%BD%D0%BE%D1%94%D0%B2%D1%80%D0%BE%D0%BF%D0%B5%D0%B9%D1%81%D1%8C%D0%BA%D0%B8%D0%BC+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B8%D0%BC+%D1%87%D0%B0%D1%81%D0%BE%D0%BC)&version=6.15.0&hosts=&consentId=cc338a3e-e5db-46f6-8dca-22061298d43a&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=%3B',
    'cto_bundle': 't5G_Bl9nbXdVZGlpSW5mZW5UZkttdWpYR0FXJTJGTURraHI5YjhJSFFMVW0waGwzcVVsekFDY0NCUEhVbDJiTUdRUHVFQiUyRjF6V0MwSDVXOWZNTm5BVUszOWY4MUd2ZEw0akRlN2pXSHllUlRMaWQlMkZBSXFGaGVTa0liTyUyRm1MVjdvWjJVQUlEemgzRWVROCUyQlhXcDFHTVdveUd0R1U4T0IyZ3lnWkthTnAwb3RFZ29GbFViR05GRUt5akV4JTJCMVVTNGlIMEVKdXJ3TXByTjJFbUE1WGhPelBxMmlFWk1OQXhpa1pWalJtTWRYaWVtdERFZjFxWGNEemgwUE04UnlHbkhwckdIY3RqTzZhNXFjQldZMFU5UlVwWFZBbDhiUEwxSE00anBNd0dUb2QzaFVWTFVrTmcyRHNpaFkxc0pwZURETFFHQ2x4Sg',
    '_ga_7XWTT00X52': 'GS1.1.1730995100.3.1.1730995808.60.0.958326608',
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

agency_with_no_agents = 0
# for agency in Agency.objects.filter(status='Done'):
def main(agency):
    print(agency)
    response = requests.get(f'https://www.athome.lu/client-agency/api/agencies/{agency.agency_id}/agents', cookies=cookies, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        if not data:
            agency_with_no_agents += 1
            print('No agents')
    else:
        print('Error:', response.status_code)

items = Agency.objects.filter(status='Done')
print(len(items))
with futures.ThreadPoolExecutor(10) as executor:
    executor.map(main, items)
    
print(agency_with_no_agents)
