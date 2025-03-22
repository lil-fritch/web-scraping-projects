from load_django import *
from parser_app.models import *
import json

for item in Business.objects.filter(status='DoneDescription').order_by('id'):
    json_data = json.loads(item.json_data_description)
    item.description_2 = json_data['specialties']
    item.history = json_data['history']['description']
    item.year_established = json_data['history']['yearEstablished']
    
    item.status = 'FullDescription'
    item.save()
    print(item, 'FullDescription')