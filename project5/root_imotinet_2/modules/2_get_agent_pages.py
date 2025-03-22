'''
Goes through saved ads and collects links to pages with agent data. 
If there is no link, it stores the agent number and name
'''

from concurrent import futures
import requests
from bs4 import BeautifulSoup

from load_django import *
from app.models import *

# for advertisement in Advertisement.objects.filter(status='New'):
def main(advertisement):
    response = requests.get(advertisement.url, allow_redirects=False)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        if 'Неактивна обява' in soup.text:
            print('Inactive ad')
            advertisement.status = 'Done'
            advertisement.save()
            return
            
        agent_info = soup.find('h6', class_='contact-agency-name')
        
        if not agent_info: 
            agent = {}
            agent_info = soup.find('div', class_='broker-agency-info')
            
            try:
                agent['agent_name'] = agent_info.find('h6', class_='broker-icon').text.strip()
            except AttributeError:
                agent['agent_name'] = None
            try:
                agent['agent_phone'] = agent_info.find('a', class_='hidden-phone').text.strip()
            except AttributeError:
                agent['agent_phone'] = None
            
            item, created = Agent.objects.get_or_create(
                agent_phone=agent['agent_phone'], 
                agent_name=agent['agent_name']
            
            )
            print(f'{created} - {item}')            

        else:
            agent_url = agent_info.find('a', class_='btn-link')['href']
        
            item, created = Pages.objects.get_or_create(
                url=agent_url
            )
            print(f'{created} - {item}')
                    
        advertisement.status = 'Done'
        advertisement.save()   
    else:
        print('Error:', response.status_code)

advertisements = Advertisement.objects.filter(status='New').order_by('id')
with futures.ThreadPoolExecutor(30) as executor:
    executor.map(main, advertisements)