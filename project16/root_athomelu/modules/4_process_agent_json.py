'''
Splits json data by field
'''

import json
from load_django import *
from parser_app.models import *

for agent in Agent.objects.filter(status="New"):
# for agent in Agent.objects.filter(pk=1):
    if not agent.json_data:
        continue
    agent_data = json.loads(agent.json_data)
    cleaned_agent_data = {key: value if value != "" else None for key, value in agent_data.items()}

    agent.agency_id = cleaned_agent_data['agencyId']
    agent.first_name = cleaned_agent_data['firstName']
    agent.last_name = cleaned_agent_data['lastName']
    agent.email = cleaned_agent_data['email']
    agent.phone_number = cleaned_agent_data['phoneNumber']
    agent.phone_extension = cleaned_agent_data['phoneExtension']
    agent.mobile_phone_number = cleaned_agent_data['mobilePhoneNumber']
    agent.mobile_phone_extension = cleaned_agent_data['mobilePhoneExtension']
    agent.virtual_phone_number = cleaned_agent_data['virtualPhoneNumber']
    agent.virtual_phone_extension = cleaned_agent_data['virtualPhoneExtension']
    agent.position = cleaned_agent_data['position']
    agent.photo_url = cleaned_agent_data['photoUrl']
    if agent.photo_url:
        agent.photo_url = 'https://i1.static.athome.eu/images/annonces2/agent/' + agent.photo_url
    agent.is_using_sms = cleaned_agent_data['isUsingSms']
    agent.is_using_whatsapp = cleaned_agent_data['isUsingWhatsapp']
    agent.is_allowing_remote_calls = cleaned_agent_data['isAllowingRemoteVisit']
    agent.experience_since = cleaned_agent_data['experienceSince']
    
    description_data = cleaned_agent_data['description']
    cleaned_description_data = {key: value if value != "" else None for key, value in description_data.items()}
    
    agent.description_de = cleaned_description_data['de']
    if agent.description_de:
        agent.description_de = agent.description_de.strip()
    agent.description_en = cleaned_description_data['en']
    if agent.description_en:
        agent.description_en = agent.description_en.strip()
    agent.description_fr = cleaned_description_data['fr']
    if agent.description_fr:
        agent.description_fr = agent.description_fr.strip()
    agent.languages = cleaned_agent_data['languages']
    
    links_data = cleaned_agent_data['links']
    cleaned_links_data = {key: value if value != "" else None for key, value in links_data.items()}
    agent.instagram_link = cleaned_links_data['instagram']
    agent.facebook_link = cleaned_links_data['facebook']
    agent.twitter_link = cleaned_links_data['twitter']
    agent.linkedin_link = cleaned_links_data['linkedin']
    agent.locale = cleaned_agent_data['locale']
    agent.status = 'Done'
    agent.save()
