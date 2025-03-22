'''
Get agent data from MyHome.ie API
'''

import requests
import json

from load_django import *
from parser_app.models import Agent

# Base URL and common query parameters
base_url = "https://api.myhome.ie/agents"

params = {
    "ApiKey": "5f4bc74f-8d9a-41cb-ab85-a1b7cfc86622",
    "CorrelationId": "c4b7902d-f441-4856-b0e0-bbc3c626db7c",
    "RequestTypeId": 10,
    "RequestVerb": "GET",
    "Endpoint": "https://api.myhome.ie/agents",
    "Region": "ireland",
    "PageSize": 20,
    "Name": ""
}

# Headers
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://myhome.ie",
    "referer": "https://myhome.ie/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

# Pagination settings
max_pages = 300  # Define the maximum number of pages you want to fetch

# Loop through pages
for page in range(1, max_pages + 1):
    # Update the page parameter for each request
    params["Page"] = page

    # Make the GET request
    response = requests.get(base_url, headers=headers, params=params)

    # Check if the response was successful
    if response.status_code == 200:
        print(f"Page {page} Response:")
        agents_data = response.json()['Agents']
        for agent in agents_data:
            agent_id = agent['GroupId']
            json_data = json.dumps(agent)
            url = 'https://www.myhome.ie/estate-agents/'+agent['UrlSlugIdentifier']+f'-{agent_id}'
            
            item, created = Agent.objects.get_or_create(
                agent_id=agent_id,
                url=url,
                json_data=json_data,
            )
            print(created, item)   

    else:
        print(f"Failed to fetch page {page}, status code: {response.status_code}")
        break  # Stop if there is an error
