"""
Gets Full Info about chat
"""

# from load_django import *
# from parser_app.models import *

import json
import requests
from time import sleep

# URL and headers
url = "https://api.superchat.de/v5/conversations"
headers = {
    'accept': '*/*',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlMta042TXRoT0t2WlFrNTdtM1ZWVyJ9.eyJodHRwczovL3N1cGVyY2hhdC5kZS9yb2xlIjoic3VwZXJ2aXNvciIsImh0dHBzOi8vc3VwZXJjaGF0LmRlL2xhbmd1YWdlIjoiZW4iLCJodHRwczovL3N1cGVyY2hhdC5kZS9wdWJsaWNVc2VySWQiOiJ1c19GNmtVTGREWEpnMHNWeE04anhDcEgiLCJodHRwczovL3N1cGVyY2hhdC5kZS9nbG9iYWxXb3Jrc3BhY2VJZCI6IjRjNzRiZTM3LTc2MTUtNDI4MS05OWExLWJmZTZkZmI0N2JlNCIsImh0dHBzOi8vc3VwZXJjaGF0LmRlL2lzU3VwZXJBZG1pbiI6bnVsbCwiaHR0cHM6Ly9zdXBlcmNoYXQuZGUvd29ya3NwYWNlU291cmNlIjoiUkVUT09MX1NBTEVTIiwiaHR0cHM6Ly9zdXBlcmNoYXQuZGUvcHVibGljVXNlckxvZ2luSWQiOiJ1c2xfOUZSR1RabUVjbXN4ZzZadWtXMm9TIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnN1cGVyY2hhdC5kZS8iLCJzdWIiOiJhdXRoMHw2NzI0ZDA0MzU1NDgzYzllMmY3NmVkZWMiLCJhdWQiOlsiaHR0cHM6Ly9hcGkuc3VwZXJjaGF0LmRlL2NvbnZlcnNhdGlvbi1zZXJ2aWNlIiwiaHR0cHM6Ly9zdXBlci1jaGF0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MzA3MjY4NDEsImV4cCI6MTczMDczNTQ0MSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBvZmZsaW5lX2FjY2VzcyIsImF6cCI6IkxRZHFGdGk2NHNyOWM5MkxhSldyVHpwNml6VDRiWmRnIn0.akGUZESpR2r2mOVRSsBsVJSMCA4M-EgxUoxWJWU4iteeHhWgY6B2dtG4r8Fojrf-AS23c1O3iG-x014yUvXLt5RWFfPasgZKQ6vl9s5Dtzyso-seMNv-RWnhcssXQRKfq0SzLYK68HTg42PLxWpDHCGW1RUkhP35dO97aiHI7Zzcjt1BTLSgPZKhs2jVT8LYxqoHLnxrQ-_0vGp4sUfDEltWn3dBTg7eMKSNhClMeQbw4hXfJsKjGMl5fYwtnt2BVYq_ezcemAAFY6cfSXGI8alr-UBcTpl5rrr5V0HaxiytKe8jKCWJPfqg2JO_n5Sg0EzYe8YoaVpe0-TTr0NR9Q',
    'content-type': 'application/json',
    'origin': 'https://app.superchat.de',
    'priority': 'u=1, i',
    'referer': 'https://app.superchat.de/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-datadog-origin': 'rum',
    'x-datadog-parent-id': '3400284807466133722',
    'x-datadog-sampling-priority': '1',
    'x-datadog-trace-id': '9139720045710942572',
    'x-superchat-platform': 'WEB',
    'x-superchat-release-timestamp': '2024-10-31T16:16:47Z',
    'x-superchat-version': 'c2f4e3fdb46b108f6d1e496f957ddf7ad7706834',
    'x-superchat-workspace-id': '4c74be37-7615-4281-99a1-bfe6dfb47be4',
}


# Parameters
params = {
    "inboxId": "ib_neMl63QAmdZKqRTDsPWTd",
    "status": "DONE",
    "sorting": "NEWEST",
    "page": 0  # Start with page 0
}

params2 = {
    'types': [
        'INBOX_MAPPING',
        'LABEL',
        'MESSAGE',
        'NOTE',
        'OPT_IN_OUT',
        'STATUS',
        'LIVE_CHAT_SESSION',
        'USER_ASSIGNMENT',
        'WHATS_APP_AD_MESSAGE',
    ],
    'page': '0',
    'size': '1000',
}

# Function to fetch conversations
def fetch_conversations(page):
    params["page"] = page
    response = requests.get(url, headers=headers, params=params)

    # Check if response is successful
    if response.status_code == 200:
        data = response.json()

        print()
        print('#' * 50)
        # print(data)
        
        conversation_data = {}
        conversations_list = data['items']
        for conversation in conversations_list:

            conversation_data['contact_name'] = conversation['contact']['displayName']
            conversation_data['contact_id'] = conversation['contact']['id']

            agents = []
            agent = {}
            for agent_data in conversation['assignedUsers']:
                agent['agent_name'] = agent_data['firstName'].strip()+ ' ' + agent_data['lastName'].strip()
                agent['id'] = agent_data['id']
                agent['photo_url'] = agent_data['profilePictureUrl']
                agents.append(agent)
            conversation_data['agents'] = agents
            
            labels = []
            label = {}
            for label_data in conversation['labels']:
                label['id'] = label_data['id']
                label['name'] = label_data['name']
                label['color'] = label_data['color']
                labels.append(label)
            conversation_data['labels'] = labels
                
            conversation_id = conversation['id']
            conversation_data['id'] = conversation_id
            conversation_data['subject'] = conversation['subject']
            conversation_data['type'] = conversation['type']
            conversation_data['status'] = conversation['status']
            conversation_data['unread_count'] = conversation['unreadCount']
            conversation_data['archived_at'] = conversation['archivedAt']
            conversation_data['highlighted'] = conversation['highlighted']
            
            response_messages = requests.get(
                f'https://api.superchat.de/v9/conversations/{conversation_id}/timeline',
                params=params2,
                headers=headers,
            )
            if response_messages.status_code == 200:
                data_messages = response_messages.json()
                
                statuses = []
                messages = []
                for message_data in data_messages['items']:
                    message = {}
                    if message_data['timelineType'] == 'MESSAGE':
                        sent_by = message_data['sentBy']
                        if sent_by:
                            message['sent_by'] = sent_by['id']
                        message['id'] = message_data['id']
                        message['text'] = message_data['payload']                      
                        message['timestamp'] = message_data['timestamp']
                        message['attachments'] = message_data['attachments']
                        message['reactions'] = message_data['reactions']
                        messages.append(message)
                    status = {}                    
                    if message_data['timelineType'] == 'CONVERSATION_STATUS':
                        status['from']  = message_data['statusFrom']
                        status['to'] = message_data['statusTo']
                        status['timestamp'] = message_data['timestamp']
                        changed_by = message_data['changedByUser']
                        if changed_by:
                            status['changed_by'] = changed_by['id']
                        statuses.append(status)
                        
                conversation_data['messages'] = messages
                conversation_data['statuses'] = statuses
                
                        
            else:
                print(f"Request failed with status code: {response_messages.status_code}")
                print("Response text:", response_messages.text)
            with open('chat.json', 'w') as f:
                json.dump(conversation_data, f, indent=4)
            break
            # for key, value in conversation_data.items():
            #     print(key+'\n', ':', value)
            print()
            # break

        return data
    else:
        print(f"Request failed with status code: {response.status_code}")

        print("Response text:", response.text)

        return None

# Loop through pages
for page in range(0, 1000):  # Adjust range as needed for more pages
    print('PAGE: ', page)
    sleep(1)
    conversations = fetch_conversations(page)
    break
    if not conversations:
        break
