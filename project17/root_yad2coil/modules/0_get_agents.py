from bs4 import BeautifulSoup
import requests

from load_django import *
from parser_app.models import Agent

cookies = {
    '_gcl_au': '1.1.869096002.1730983333',
    '_gid': 'GA1.2.892878992.1730983334',
    'ndl-fonts-loaded': 'true',
    'keystone.sid': 's%3Aa1919d8f-2645-458c-8d9c-c2f5f478df79.fFjAc3vXqCzjdnEndY1jxGjKJ9Yongzf7mbocVfX5rc',
    '_pk_ref.2d3af2ef-d791-457d-bc0a-243b29fdd6a7.45b2': '%5B%22%22%2C%22%22%2C1731078756%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.2d3af2ef-d791-457d-bc0a-243b29fdd6a7.45b2': '*',
    '_dc_gtm_UA-2802802-1': '1',
    '_ga_71S9VQGFT2': 'GS1.1.1731078756.9.1.1731080577.60.0.0',
    '_ga': 'GA1.1.369034660.1730983334',
    '_ga_5EDCKYSLXL': 'GS1.1.1731078756.9.1.1731080577.60.0.0',
    '_ga_RDB65G8M6W': 'GS1.1.1731078757.9.1.1731080577.60.0.0',
    '_ga_6CE5WZCBZC': 'GS1.1.1731078757.9.1.1731080577.60.0.0',
    '_ga_VNXCGC8D2Y': 'GS1.1.1731078756.9.1.1731080577.60.0.0',
    '_pk_id.2d3af2ef-d791-457d-bc0a-243b29fdd6a7.45b2': 'b6589fc6ab0dc82c.1730983333.7.1731080597.1731078756.',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-none-match': 'W/"157df-uJqVRNVpAdm/57/K5phNG4LaudI"',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

for page in range(1, 10):
    response = requests.get(f'https://www.nadlan.com/agents/{page}', cookies=cookies, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        agents = soup.find_all('div', {'class': 'company-item'})
        if len(agents) == 0:
            break
        agent = {}
        for agent_data in agents:
            try:
                agent['name'] = agent_data.find('a', {'class':'title shared dotdotdot'}).text
            except AttributeError:
                agent['name'] = None
            try:
                agent['phone'] = agent_data.find('span', {'class':'info-small phone desktop'}).text
            except AttributeError:
                agent['phone'] = None
            try:
                photo_id = agent_data.find('img', {'class':'sft-responsive'})['data-src']
                if photo_id:
                    agent['photo_url'] = 'https://cdn.nadlan.com/w-272/' + photo_id
                else:
                    agent['photo_url'] = 'https://www.nadlan.com/media/images/defaults/140-140.jpg'
            except AttributeError:
                agent['photo_url'] = None
            try:
                agent['description'] = agent_data.find('div', {'class':'description dotdotdot'}).text
                agent['description'] = agent['description'].strip()
            except AttributeError:
                agent['description'] = None

            item, created = Agent.objects.get_or_create(
                phone=agent['phone'], 
                defaults=agent
            )
            print(created, item)
            
    else:
        print(f'Error: {response.status_code}')
        break            