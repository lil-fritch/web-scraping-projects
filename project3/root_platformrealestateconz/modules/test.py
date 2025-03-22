import requests
import json

from load_django import *
from app.models import Agent

items = Agent.objects.all()
for item in items:
    if item.office_image:
        item.office_image = 'https://mediaserver.realestate.co.nz'+item.office_image+'.scale.x40.jpg'
        
        item.save()
        print('Saved:', item.agent_id)