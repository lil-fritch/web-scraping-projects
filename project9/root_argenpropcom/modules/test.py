

import re
from bs4 import BeautifulSoup
import requests

cookies = {
    '_scor_uid': '91b7800c02ff4afc807aea6efc154478',
    '_ga': 'GA1.1.1073552201.1730390990',
    '_hjSessionUser_3427973': 'eyJpZCI6ImYyNTU3NWFjLWE1MGMtNWI5YS1hZjJhLTVlZDg0OTg4MmVjOCIsImNyZWF0ZWQiOjE3MzAzOTA5ODk5MjgsImV4aXN0aW5nIjp0cnVlfQ==',
    'area': 'LatLng(-34.9426%2C-58.1133)%2CLatLng(-34.9426%2C-58.0627)%2CLatLng(-34.9426%2C-58.0120)%2CLatLng(-34.9697%2C-58.0120)%2CLatLng(-34.9697%2C-58.0627)%2CLatLng(-34.9697%2C-58.1133)',
    '_hjDonePolls': '902973',
    'g_state': '{"i_l":0}',
    '_pmb_session_token_': '25B043BE4F0225817CB3CA460A63587689DF688D70D0FBF28528CC83C4FA44B63AC1697431410D8E2BD77735150B2C5AD9CFFC36AEF5CF400610B00062023967386B590A6BB8FD272F1D5B542BBD52A73816348357F18EE5A1EBCBA3A84CE930D19A7015122157963929A2DB38B44A7B1978B1EF4EC2C57F81422EF5E4ECD50A',
    '_hjSession_3427973': 'eyJpZCI6ImIxN2NiZjk2LWZkZGItNDE4OC04NTYzLTQ2MjNmOTlhMjI2MSIsImMiOjE3MzA0MDEzMjI2MjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    '.AspNetCore.Antiforgery.7VAPn8AcYdQ': 'CfDJ8P0KTcMsSQNIuP2_7YFi4kaRqJ2rEGib5nSsoCgG-N4itN7hjR-8ZgpH-N7-7l1sX5vhnFryYOZm5be356GQvOVvWkm6I4aSaIBTXY--pCP8G3Q_oBk-pQZfrsyUJWUMZU50PIgefFQYjJsp8TVhZqM',
    '_gcl_au': '1.1.462102648.1730390990.1757495762.1730401401.1730401518',
    '_uetsid': '8e7d15b097a211ef8ad9153450857446',
    '_uetvid': '8e7d34c097a211efb521cb3261c5da24',
    '_ga_X0E5QSKP69': 'GS1.1.1730401322.2.1.1730401522.57.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.argenprop.com/inmobiliarias?Nombre=aaa&Orden=CantidadAvisos',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

alphabet = 'abcdefghijklmnopqrstuvwxyz'

respone = requests.get(
    f'https://www.argenprop.com/inmobiliarias?Orden=CantidadAvisos&Nombre=ber',
    headers=headers,
    cookies=cookies
    )

if respone.status_code == 200:
    
    soup = BeautifulSoup(respone.text, 'html.parser')
    agents_data = soup.find_all('div', class_='card-agent')
    
    agent = {}
    for agent_data in agents_data:
        whatsapp = agent_data.find('button', class_='btn btn-icon--wa')
        if whatsapp:
            try:                            
                whatsapp_url = whatsapp.get('data-wa-href')
                agent['phone'] = re.search(r'wa\.me/(\d+)', whatsapp_url).group(1)
            except AttributeError:
                agent['phone'] = None
            try:
                agent['name'] = agent_data.find('div', class_='card-agent-title').text.strip()
            except AttributeError:
                agent['name'] = None
            try:
                location_icon = agent_data.find('i', class_='basico1-icon-compass')
                if location_icon:
                    agent['location'] = location_icon.find_next('span').text.strip()
                else:
                    agent['location'] = None
            except AttributeError:
                agent['location'] = None
            try:
                address_icon = agent_data.find('i', class_='basico1-icon-marker')
                if address_icon:
                    agent['address'] = address_icon.find_next('span').text.strip()
                else:
                    agent['address'] = None
            except AttributeError:
                agent['address'] = None
            try:
                properties_icon = agent_data.find('i', class_='basico1-icon-sell')
                if properties_icon:
                    agent['properties'] = properties_icon.find_next('span').text.strip()
                else:
                    agent['properties'] = None
            except AttributeError:
                agent['properties'] = None
            try:
                agent['image'] = agent_data.find('img', class_='card-agent-logo').get('data-src')
            except AttributeError:
                agent['image'] = None            
            
            for key, value in agent.items():
                print(f'{key}: {value}')
            print()
else:
    print(f'Error: {respone.status_code}')