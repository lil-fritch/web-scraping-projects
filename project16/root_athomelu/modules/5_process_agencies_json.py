'''
Splits json data by field
'''

from load_django import *
from parser_app.models import *

import json
# for agency in Agency.objects.filter(pk=1):
for agency in Agency.objects.filter(status='New'):
    agency_data = json.loads(agency.json_data)
    cleaned_agency_data = {key: value if value != "" else None for key, value in agency_data.items()}
    print(cleaned_agency_data)
    agency.agency_id = cleaned_agency_data['id']
    agency.agency_name = cleaned_agency_data['name']
    agency.account_site = cleaned_agency_data['account_site']
    agency.website = cleaned_agency_data['website']
    agency.addresses = json.dumps(agency_data['addresses'])
    agency.recommendations = agency_data['recommendations']
    
    facets_data = cleaned_agency_data['facets']
    cleaned_facets_data = {key: value if value != "" else None for key, value in facets_data.items()}
    
    agency.facets_buy = cleaned_facets_data['buy']
    agency.facets_rent = cleaned_facets_data['rent']
    agency.facets_sold = cleaned_facets_data['sold']
    
    agency.followers = cleaned_agency_data['followers']   
    agency.logo_url = cleaned_agency_data['logo']
    if agency.logo_url:
        agency.logo_url = 'https://i1.static.athome.eu/logoagences/' + agency.logo_url
    
    agency.status = 'Done'
    agency.save()