'''
Goes through all categories and pages and saves agents to the database
'''
from concurrent import futures
import json
import re
import requests
from bs4 import BeautifulSoup

from load_django import *
from parser_app.models import *

def main(category):
    for page in range(1, 2000):
        
        if page == 1: url = category.url
        else: url = f'{category.url}/strana-{page}'
            
        print(f'Parsing {category.name} page {page}')
        
        response = requests.get(url, allow_redirects=False)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            script_content = soup.find('script', string=re.compile(r'var results'))

            json_string = re.search(r'var results\s*=\s*(\{.*?\});', script_content.string, re.DOTALL).group(1)

            results_value = json.loads(json_string)
            all_posts = results_value['content']
            
            agent = {}
            for post in all_posts:
                post = post['createdByUser']
                try:
                    agent['agent_id'] = post['id']
                except AttributeError:
                    agent['agent_id'] = None
                try:
                    agent['first_name'] = post['firstName']
                except AttributeError:
                    agent['first_name'] = None
                try:
                    agent['last_name'] = post['lastName']
                except AttributeError:
                    agent['last_name'] = None
                try:
                    agent['phone'] = post['phoneNumber']
                except AttributeError:
                    agent['phone'] = None
                try:
                    agent['email'] = post['email']
                except AttributeError:
                    agent['email'] = None
                try:
                    agent['agency'] = post['agency']
                except AttributeError:
                    agent['agency'] = None
                try:
                    agent['profile_image'] = post['profileImage']
                    if agent['profile_image']:
                        agent['profile_image'] = 'https://content.estitor.com/'+ str(agent['profile_image']).split('.')[0] + '-xs.webp'
                except AttributeError:
                    agent['profile_image'] = None
                try:
                    agent['is_verified'] = post['isVerified']
                except AttributeError:
                    agent['is_verified'] = None

                item, created = Agent.objects.get_or_create(
                    agent_id=agent['agent_id'],
                    defaults=agent
                )
                print(f'{created}: {item}')
                
        elif response.status_code == 301:
            print('End of pages')
            break
        
        else:
            print(f'Error: {response.status_code}')
    
    category.status = 'Done'
    category.save()       

categories = Category.objects.filter(status="New").order_by('id')
with futures.ThreadPoolExecutor(3) as executor:
    executor.map(main, categories)