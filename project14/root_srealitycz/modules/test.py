from load_django import *
from parser_app.models import *

items = Agent.objects.filter(status="Done")
for item in items:
    if not item.agency_website:
        item.agency_website = None

        
    item.save()
    print(item)