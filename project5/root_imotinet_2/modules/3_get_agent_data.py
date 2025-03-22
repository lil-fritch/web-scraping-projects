from concurrent import futures
import requests
from bs4 import BeautifulSoup

from load_django import *
from app.models import *

agent = {}
# for page in Pages.objects.filter(status='New'):
def main(page):        
    response = requests.get(page.url)
    
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        agency_block = soup.find('div', class_='broker-agency-info')
        try:
            agent['agency_photo'] = agency_block.find('img')
            if agent['agency_photo']:
                agent['agency_photo'] = 'https://ekipimoti.imoti.net' + agent['agency_photo']['src']
            else:
                agent['agency_photo'] = None
        except AttributeError:
            agent['agency_photo'] = None
        try:
            agent['agency_name'] = soup.find('ul', class_='contacts').find('h4').text.strip()
        except AttributeError:
            agent['agency_name'] = None
        try:
            agent['agency_email'] = agency_block.find('span', class_='contact-mail').text.strip()
        except AttributeError:
            agent['agency_email'] = None
        try:
            agent['agency_phone'] = agency_block.find('span', class_='contact-tel').text.strip()
        except AttributeError:
            agent['agency_phone'] = None
        try:
            agent['agency_adress'] = agency_block.find('span', class_='contact-address').text.strip()
        except AttributeError:
            agent['agency_adress'] = None
        try:
            agent['agency_contact_link'] = agency_block.find('span', class_='contact-link')
            if agent['agency_contact_link']:
                agent['agency_contact_link'] = agent['agency_contact_link'].find('a')['href']
        except AttributeError:
            agent['agency_contact_link'] = None
        try:
            agent['agency_contact_link_2'] = agency_block.find('span', class_='contact-link2')
            if agent['agency_contact_link_2']:
                agent['agency_contact_link_2'] = agent['agency_contact_link_2'].find('a')['href']
            else:
                agent['agency_contact_link_2'] = None
        except AttributeError:
            agent['agency_contact_link_2'] = None
            
        agents_block = soup.find('ul', class_='contacts col-2')
        agents_info = agents_block.find_all('div', class_='broker-agency-info')
        for agent_info in agents_info:
            try:
                agent['agent_name'] = agent_info.find('h4', class_='broker-name').text.strip()
            except AttributeError:
                agent['agent_name'] = None
            try:
                agent['agent_photo'] = agent_info.find('img')
                if agent['agent_photo']:
                    agent['agent_photo'] = 'https://ekipimoti.imoti.net' + agent['agent_photo']['src']
                else:
                    agent['agent_photo'] = None
            except AttributeError:
                agent['agent_photo'] = None
            try:
                agent['agent_phone'] = agent_info.find('span', class_='contact-tel').text.strip()
            except AttributeError:
                agent['agent_phone'] = None
            try:
                agent['agent_adress'] = agent_info.find('span', class_='contact-address').text.strip()
            except AttributeError:
                agent['agent_adress'] = None
            try:
                agent['is_trusted'] = bool(agent_info.find('div', class_='recommended-badge broker'))
            except AttributeError:
                agent['is_trusted'] = False

            item, created = Agent.objects.get_or_create(
                agent_phone=agent['agent_phone'],
                defaults=agent
            )
            print(f'{created}: {item}')
    
        page.status = 'Done'
        page.save()
        
    else:
        print('Error:', response.status_code)        

pages = Pages.objects.filter(status='New')
with futures.ThreadPoolExecutor(25) as executor:
    executor.map(main, pages)