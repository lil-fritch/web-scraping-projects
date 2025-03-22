import requests
import json

from load_django import *
from app.models import Agent

agents = Agent.objects.filter(status='New').order_by('id')
for agent in agents:
    agent_id = agent.agent_id
    
    json_data = agent.json_data
    agent_data = json.loads(json_data)
    
    attributes = agent_data['attributes']
    
    agent.agents_of_excellence_rank = attributes.get('agents-of-excellence-rank')
    agent.blog_url = attributes.get('blog-url')
    agent.email = attributes.get('email')
    agent.facebook_url = attributes.get('facebook-url')
    agent.first_name = attributes.get('first-name')
    image = attributes.get('image')
    if image: 
        agent.image = image.get('base-url')
    agent.job_title = attributes.get('job-title')
    agent.last_name = attributes.get('last-name')
    agent.linkedin_url = attributes.get('linkedin-url')
    agent.listing_count = attributes.get('listing-count')
    agent.name = attributes.get('name')
    agent.office_brand_hex_code = attributes.get('office-brand-hex-code')
    agent.office_image = attributes.get('office-image')
    agent.office_is_brand_colour_light = attributes.get('office-is-brand-colour-light')
    agent.office_name = attributes.get('office-name')
    agent.phone = attributes.get('phone')
    agent.phone_ddi = attributes.get('phone-ddi')
    agent.phone_mobile = attributes.get('phone-mobile')
    agent.show_profile = attributes.get('show-profile')
    agent.slug = attributes.get('slug')
    agent.twitter_url = attributes.get('twitter-url')
    agent.website_url = attributes.get('website-url')
    
    agent.status = 'Done'
    agent.save()
    print('Saved:', agent_id)