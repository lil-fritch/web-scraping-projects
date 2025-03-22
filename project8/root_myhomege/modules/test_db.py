from load_django import *
from parser_app.models import *

agents = Agent.objects.filter(status='Done').order_by('id')
print(len(agents))