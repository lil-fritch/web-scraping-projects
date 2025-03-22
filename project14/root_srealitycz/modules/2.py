import json
from load_django import *
from parser_app.models import *

items = Agent.objects.filter(status="New")
# items = Agent.objects.filter(pk=1)
for item in items:
    agency_data = json.loads(item.agency_json)
    agent_data = json.loads(item.agent_json)
    
    item.ico = agency_data.get('ico')
    item.name = agent_data.get('name')
    
    phones = []
    for phone in agent_data.get('phones'):
        phones.append(phone.get('phone'))
    item.phones = phones
    
    item.email = agent_data.get('email')
    item.image = agent_data.get('image')
    if item.image:
        item.image = 'https:' + item.image + '?fl=res,200,300,3|shr,,20|webp,75'
    item.rating = agent_data.get('rating')
    item.review_count = agent_data.get('reviewCount')
    
    item.agency_name = agency_data.get('name')
    item.agency_email = agency_data.get('email')
    item.agency_phone = agency_data.get('phone')
    if item.agency_phone:
        item.agency_phone = item.agency_phone.get('phone')
    item.agency_id = agency_data.get('id')
    item.agency_image = agency_data.get('logo')
    item.agency_website = agency_data.get('visibleWww')
    
    item.status = "Done"
    item.save()