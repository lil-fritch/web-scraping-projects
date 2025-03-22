'''
Retrieves json from the database and distributes data from it 
to the appropriate fields of the model
'''

import json
from load_django import *
from parser_app.models import *


for agent_data in Agent.objects.filter(status='New').order_by('id'):
    agent_json = json.loads(agent_data.agent_json)
    agency_json = json.loads(agent_data.agency_json)
    
    agent_data.full_name = agent_json['fullname']
    agent_data.phone = agent_json['phone']
    agent_data.st_count = agent_json['st_count'][0]
    
    agent_data.agency_id = agency_json['makler_id']
    agent_data.agency_name = agency_json['makler_name']
    agent_data.agency_phones = agency_json['phones']
    agent_data.agency_type_id = agency_json['makler_type_id']
    agent_data.agency_creator_id = agency_json['user_id']
    agent_data.has_logo = agency_json['has_logo']
    agent_data.logo_ver = agency_json['logo_ver']
    agent_data.agency_st_count = agency_json['st_count'][0]
    agent_data.address_geo = agency_json['address_geo']
    agent_data.address_eng = agency_json['address_eng']
    agent_data.address_ru = agency_json['address_ru']
    
    agent_data.status = 'Done'
    agent_data.save()
    print('Saved: ' + agent_data.agent_id) 