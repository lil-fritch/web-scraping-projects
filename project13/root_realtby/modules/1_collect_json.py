'''
Collects json for all agents
'''

import requests
import json

from load_django import *
from parser_app.models import *

# URL and headers for the GraphQL endpoint
url = "https://realt.by/bff/graphql"
headers = {
    "authority": "realt.by",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "origin": "https://realt.by",
    "referer": "https://realt.by/realtors/?page=5",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-realt-client": "www@4.6.0",
    "cookie": "realt_user=e7d613053df6634db02c72b899e74440; _gcl_au=1.1.1047659875.1730380904; _fbp=fb.1.1730380903789.974812480419964710; gdprConfirmed=1; consent={%22analytics%22:true%2C%22advertising%22:true%2C%22functionality%22:true}; _ga=GA1.2.495014094.1730380904; _ga_3RLZ0E8JHQ=GS1.2.1730380903.1.1.1730380948.15.0.1152550604",
}

# Pagination parameters
page_size = 2000   # Number of results per page
max_pages = 10   # Maximum number of pages to fetch

for page in range(1, max_pages + 1):
    # Update the payload with the current page number
    payload = json.dumps([
        {
            "operationName": "agentsListing",
            "variables": {
                "data": {
                    "where": {
                        "stateRegionUuid": "499f06b8-7b00-11eb-8943-0cc47adabd66"
                    },
                    "sort": [
                        {"by": "promote", "order": "DESC"},
                        {"by": "sorting", "order": "DESC"},
                        {"by": "id", "order": "DESC"}
                    ],
                    "pagination": {
                        "page": page,
                        "pageSize": page_size
                    }
                }
            },
            "query": """fragment AgentsPagination on AgentsListing {
                            pagination {
                                page
                                pageSize
                                totalCount
                                __typename
                            }
                            __typename
                        }

                        query agentsListing($data: AgentsListingInput!) {
                            agentsListing(data: $data) {
                                ...AgentsPagination
                                results {
                                    id
                                    agentUuid
                                    userUuid
                                    userId
                                    firstName
                                    lastName
                                    avatarUuid
                                    avatarName
                                    avatarExt
                                    position
                                    occupationId
                                    occupationTitle
                                    primarySpecializationId
                                    primarySpecializationTitle
                                    specializations
                                    email
                                    phones
                                    workRegions {
                                        type
                                        dictionaryUuid
                                        data {
                                            uuid
                                            title
                                            type
                                            townName
                                            __typename
                                        }
                                        __typename
                                    }
                                    deleted
                                    confirmed
                                    updatedAt
                                    sorting
                                    viewsCount
                                    isAvatar
                                    agencyUuid
                                    agencyTitle
                                    agencyLogoUuid
                                    agencyLogoName
                                    agencyLogoExt
                                    agencySlug
                                    agencyOBDNUuid
                                    agencyOBDNTitle
                                    rating
                                    reviewsCount
                                    promote
                                    __typename
                                }
                                __typename
                            }
                        }"""
        }
    ])

    # Make the POST request for the current page
    response = requests.post(url, headers=headers, data=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()[0]['data']['agentsListing']['results']
        for agent_data in data:

            item, created = Agent.objects.get_or_create(
                agent_id = agent_data['id'],
                json_data = json.dumps(agent_data)
            )
                
            print(created, item)
        break
    else:
        print(f"Failed to fetch page {page}, status code: {response.status_code}")
        break  # Stop the loop if there is an error
