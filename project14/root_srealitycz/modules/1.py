import requests
from bs4 import BeautifulSoup
import json

from load_django import *
from parser_app.models import *

items = Agency.objects.filter(status="New")
for item in items:
    response = requests.get(item.url)
    soup = BeautifulSoup(response.text, "html.parser")

    next_data_script = soup.find("script", id="__NEXT_DATA__")

    if next_data_script:
        next_data = json.loads(next_data_script.string)
        try:
            agency_data = next_data["props"]["pageProps"]["dehydratedState"]["queries"][1]['state']['data']
            agents_data = next_data["props"]["pageProps"]["dehydratedState"]["queries"][5]['state']['data']
        except Exception as e:
            print("Error: ", e)
            continue
        for agent_data in agents_data['pages'][0]['results']:
            
            agent_id = agent_data['id']
            agent_data = json.dumps(agent_data)
            keys_to_keep = ['email', 'name', 'phone', 'visibleWww', 'id', 'logo']
            filtered_agency_data = {k: agency_data[k] for k in keys_to_keep if k in agency_data}
            
            filtered_agency_data = json.dumps(filtered_agency_data)
            
            agent, created = Agent.objects.get_or_create(
                agent_id=agent_id,
                agency_json = filtered_agency_data,
                agent_json = agent_data
            )
            print(created, agent)    
        
        item.status = "Done"
        item.save()
    else:
        print("Скрипт з '__NEXT_DATA__' не знайдений на сторінці")
