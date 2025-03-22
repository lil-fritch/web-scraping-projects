'''
Gets json from the database and splits data into fields
'''

import json
from load_django import *
from parser_app.models import *

agents_data = Agent.objects.filter(status='New')
for agent in agents_data:
    agent_json = json.loads(agent.json_data)
    
    agent.account_number = agent_json['accountnumber']
    agent.email_address = agent_json['emailaddress1']
    agent.telephone_1 = agent_json['telephone1']
    agent.telephone_2 = agent_json['telephone2']
    agent.name = agent_json['name']
    agent.cpa_trading_name = agent_json['cpa_tradingname']
    agent.websiteurl = agent_json['websiteurl']
    agent.address_composite = agent_json['address2_composite']
    agent.address_latitude = agent_json['address2_latitude']
    agent.address_longitude = agent_json['address2_longitude']
    agent.status = 'Done'
    agent.save()
    print(agent, 'Updated')    