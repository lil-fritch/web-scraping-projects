'''
Gets all the unique IDs of the agencies, 
goes through their pages and collects the rest of the data from there
'''

from concurrent import futures
import requests
from bs4 import BeautifulSoup

from load_django import *
from parser_app.models import *

url = "https://www.myhome.ge/ka/makler?makler_id=7393"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "max-age=0",
    "Referer": "https://www.myhome.ge/ka/maklers/?makler_type_id=1",
    "Upgrade-Insecure-Requests": "1",
}

def decode_email(encoded_email):
    def hex_to_int(hex_str):
        return int(hex_str, 16)

    def decrypt(encoded, start):
        key = hex_to_int(encoded[start:start + 2])
        decrypted_chars = []

        for i in range(start + 2, len(encoded), 2):
            char_code = hex_to_int(encoded[i:i + 2]) ^ key
            decrypted_chars.append(chr(char_code))

        return ''.join(decrypted_chars)

    if encoded_email.startswith('/cdn-cgi/l/email-protection#'):
        encoded_email = encoded_email.split('#')[1]  

    decoded_email = decrypt(encoded_email, 0) 

    return decoded_email

def generate_logo_link(agent):
    if agent.has_logo == '1':
        url = f'https://static.my.ge/myhome/maklers/logos/{agent.agency_id}.jpg?v={agent.logo_ver}'
    else:
        url = None
    return url

def generate_banner_link(agent):
    if agent.has_logo == '1':
        url = f'https://static.my.ge/myhome/developers/photos/covers/large/{agent.agency_id}_1.jpg?ver=1'
    else:
        url = None
    return url

unique_agency_ids = Agent.objects.values('agency_id').distinct()

agents = []
for agency_id in unique_agency_ids:
    agent = Agent.objects.filter(agency_id=agency_id['agency_id']).first()
    if agent:
        agents.append(agent)

email = None
# for agent in agents:
def main(agent):
    response = requests.get(f'https://www.myhome.ge/ka/makler?makler_id={agent.agency_id}', headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        email_elements = soup.select('a.__cf_email__')
        for element in email_elements:
            email = decode_email(element['data-cfemail'])
        
        if not email_elements:
            email = None
            
        logo_url = generate_logo_link(agent)
        banner_url = generate_banner_link(agent)
    
    else:
        print(f"Error: {response.status_code}")
        agents = Agent.objects.filter(agency_id=agent.agency_id)
        
    for agent in agents:
        agent.agency_email = email
        agent.agency_logo = logo_url
        agent.agency_banner = banner_url
        agent.save()
        
        print(f'Data for {agent.agent_id} updated')
        
with futures.ThreadPoolExecutor(10) as executor:
    executor.map(main, agents)