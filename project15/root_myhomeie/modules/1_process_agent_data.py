'''
Get the agent data from the database and update the agent model with the data.
'''

from load_django import *
from parser_app.models import Agent

import json

for item in Agent.objects.filter(status="New"):
    
    agent_data = json.loads(item.json_data)
    
    item.name = agent_data.get('Name', None)
    item.phone = agent_data.get('DisplayPhone', None)
    item.seo_name = agent_data.get('SeoName', None)
    item.address = agent_data.get('Address', None)
    item.image_url = agent_data.get('LogoUrl', None)
    item.sales_license = agent_data.get('SalesLicense', None)
    if not item.sales_license:
        item.sales_license =  None
    item.rental_license = agent_data.get('RentalLicense', None)
    if not item.rental_license:
        item.rental_license =  None
    item.is_phone_revealed = agent_data.get('IsPhoneRevealed', None)
    
    item.status = "Done"
    item.save()