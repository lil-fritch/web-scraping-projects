'''
Goes through the pages of agencies 
and collects information about agents and the agencies themselves
'''
from bs4 import BeautifulSoup
import requests
from load_django import *
from parser_app.models import Agency, Agent

cookies = {
    'SLINGSHOT': 'LanguageCode=he-IL',
    'SessionId': '',
    'ASP.NET_SessionId': 'duykmlbe052fh1554d011yxw',
    'SelectedModeCookie': 'residential',
    '_gcl_au': '1.1.1712061631.1731080166',
    '_gid': 'GA1.2.1948804951.1731080167',
    '__utmc': '136538803',
    '__utmz': '136538803.1731080204.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utma': '136538803.1647375933.1731080167.1731080204.1731083242.2',
    '__utmb': '136538803.8.10.1731083242',
    'clix.session': '6068341745932346',
    '_gat_UA-1993435-2': '1',
    '_ga_MKYRY78B5M': 'GS1.1.1731083241.2.1.1731085263.3.0.0',
    '_ga': 'GA1.2.1647375933.1731080167',
    '_gat': '1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.remax-israel.com/officeagentsearch.aspx',
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

for agency in Agency.objects.filter(status="New"):
    response = requests.get(
        url=agency.url,
        cookies=cookies,
        headers=headers,
    )   
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        agent = {}
        try:
            agent['agency_name'] = soup.find('h2').text.strip()
        except:
            agent['agency_name'] = None
        try:
            agent['agency_office_phone'] = soup.find('span', itemprop='telephone').text.strip()
        except:
            agent['agency_office_phone'] = None 
        agent['agency_office_fax'] = agency.office_fax
        try:
            agent['agency_address'] = soup.find('span', class_='office-address').text.strip()
        except:
            agent['agency_address'] = None
        try:
            agent['agency_photo'] = soup.find('img', itemprop='image')['src']
            if agent['agency_photo'] == '/common/images/default_image_office.gif':
                agent['agency_photo'] = 'https://www.remax-israel.com/common/images/default_image_office.gif'
        except:
            agent['agency_photo'] = None
        agent['agency_url'] = agency.url
        
        agents = soup.find_all('div', class_='our-agents-item')
        for agent_data in agents:
            try:
                agent['agent_photo'] = agent_data.find('img', class_='img-responsive')['src']
                if agent['agent_photo'] == '/common/images/default_image_agent_sm.gif':
                    agent['agent_photo'] = 'https://www.remax-israel.com/common/images/default_image_agent_sm.gif'
                elif agent['agent_photo'] == '/common/images/default_image_office.gif':
                    agent['agent_photo'] = 'https://www.remax-israel.com/common/images/default_image_office.gif'
            except:
                agent['agent_photo'] = None
            try:
                agent['agent_name'] = agent_data.find('span', class_='agent-name').text.strip()
            except:
                agent['agent_name'] = None
            try:
                agent['agent_license'] = agent_data.find('span', class_='agent-licenseid creci_num').text.replace('מספר רישיון:', '').strip()
                if not agent['agent_license']:
                    agent['agent_license'] = None
            except:
                agent['agent_license'] = None
            try:
                agent['agent_url'] = agent_data.find('a')['href']
            except:
                agent['agent_url'] = None
            
            item, created = Agent.objects.get_or_create(
                agent_name=agent['agent_name'], 
                defaults=agent
            )
            print(created, item)
        agency.status = "Parsed"
        agency.save()
    else:
        print(response.status_code)
        break