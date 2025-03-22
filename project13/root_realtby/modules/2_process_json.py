'''
Gets json from the database and splits it into fields
'''

import json
from load_django import *
from parser_app.models import *

for item in Agent.objects.filter(status='New'):
    agent_data = json.loads(item.json_data)

    item.agent_uuid = agent_data['agentUuid']
    item.user_uuid = agent_data['userUuid']
    item.user_id = agent_data['userId']
    item.first_name = agent_data['firstName']
    item.last_name = agent_data['lastName']
    item.avatar_uuid = agent_data['avatarUuid']
    item.avatar_name = agent_data['avatarName']
    item.avatar_ext = agent_data['avatarExt']
    item.position = agent_data['position']
    if not item.position:
        item.position = None
    item.occupation_id = agent_data['occupationId']
    item.occupation_title = agent_data['occupationTitle']
    item.primary_specialization_id = agent_data['primarySpecializationId']
    item.primary_specialization_title = agent_data['primarySpecializationTitle']
    item.specializations = agent_data['specializations']
    item.email = agent_data['email']
    
    phones= []
    phones_data = agent_data['phones']
    if phones_data:
        for phone in phones_data:
            phones.append(phone.strip())
        if len(phones) == 1:
            phones = phones[0]
    else:
        phones = None
    item.phones = phones
    
    regions = []
    for region in agent_data['workRegions']:
        town_name = region['data']['townName']
        title = region['data']['title'].strip()
        if town_name:
            regions.append(f'{town_name.strip()} - {title}')
        else:
            regions.append(title)
    item.work_regions = regions        
        
    item.deleted = agent_data['deleted']
    item.confirmed = agent_data['confirmed']
    item.updated_at = agent_data['updatedAt']
    item.sorting = agent_data['sorting']
    item.views_count = agent_data['viewsCount']
    item.is_avatar = agent_data['isAvatar']
    item.agency_uuid = agent_data['agencyUuid']
    item.agency_title = agent_data['agencyTitle']
    item.agency_logo_uuid = agent_data['agencyLogoUuid']
    item.agency_logo_name = agent_data['agencyLogoName']
    item.agency_logo_ext = agent_data['agencyLogoExt']
    item.agency_slug = agent_data['agencySlug']
    item.agency_obdn_uuid = agent_data['agencyOBDNUuid']
    item.agency_obdn_title = agent_data['agencyOBDNTitle']
    item.rating = agent_data['rating']
    item.reviews_count = agent_data['reviewsCount']
    item.promote = agent_data['promote']
    item.type_name = agent_data['__typename']
    
    item.status = 'Done'
    item.save()
    print(item, 'Updated')
    
    