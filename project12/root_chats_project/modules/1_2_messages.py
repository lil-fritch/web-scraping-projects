'''
Go through saved conversations and get all messages from them
'''

from concurrent import futures
import time
from load_django import *
from parser_app.models import *

import json
import requests


headers = {
    'accept': '*/*',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlMta042TXRoT0t2WlFrNTdtM1ZWVyJ9.eyJodHRwczovL3N1cGVyY2hhdC5kZS9yb2xlIjoiYWRtaW4iLCJodHRwczovL3N1cGVyY2hhdC5kZS9sYW5ndWFnZSI6ImVuIiwiaHR0cHM6Ly9zdXBlcmNoYXQuZGUvcHVibGljVXNlcklkIjoidXNfRjZrVUxkRFhKZzBzVnhNOGp4Q3BIIiwiaHR0cHM6Ly9zdXBlcmNoYXQuZGUvZ2xvYmFsV29ya3NwYWNlSWQiOiI0Yzc0YmUzNy03NjE1LTQyODEtOTlhMS1iZmU2ZGZiNDdiZTQiLCJodHRwczovL3N1cGVyY2hhdC5kZS9pc1N1cGVyQWRtaW4iOm51bGwsImh0dHBzOi8vc3VwZXJjaGF0LmRlL3dvcmtzcGFjZVNvdXJjZSI6IlJFVE9PTF9TQUxFUyIsImh0dHBzOi8vc3VwZXJjaGF0LmRlL3B1YmxpY1VzZXJMb2dpbklkIjoidXNsXzlGUkdUWm1FY21zeGc2WnVrVzJvUyIsImlzcyI6Imh0dHBzOi8vYXV0aC5zdXBlcmNoYXQuZGUvIiwic3ViIjoiYXV0aDB8NjcyNGQwNDM1NTQ4M2M5ZTJmNzZlZGVjIiwiYXVkIjpbImh0dHBzOi8vYXBpLnN1cGVyY2hhdC5kZS9jb252ZXJzYXRpb24tc2VydmljZSIsImh0dHBzOi8vc3VwZXItY2hhdC5ldS5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNzMwNzg3NzMzLCJleHAiOjE3MzA3OTYzMzMsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJMUWRxRnRpNjRzcjljOTJMYUpXclR6cDZpelQ0YlpkZyJ9.Zk_T0yAaECTHcxYa68OB_p8GJmnOxP6vOOiiDeTCVxB_8KkjxHCSQa2LOSdRjCwpQ7jnwvNuc3ebSpnmtdHO45X-bXczk8mqLf0FqHbJlnEqqIejnasUtM99B7nGs5bMNzJW8k8EHAtYg-UZ6lngVO87CBtAe_TcZZcIhKkvkq_092oLNnDKHzUZm5l4ViZDHvqKUcgg7YW-s7seVSr-pihbWArYBudHYTDN6uVTDeKLFyAM2LNE9leV8XToO7HoO9R3_p6G3MVfHsCw5UlXHdWxO4b4ockvaZT2RR5p5oWPV3tynWgZm1sFT5e1XZTRhPnl0T8Scl3vvCTul00zhA',
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
    'x-superchat-platform': 'WEB',
    'x-superchat-release-timestamp': '2024-11-04T18:12:12Z',
    'x-superchat-version': '49078d799f90a6a542d445fd3121fb12f5b63f81',
    'x-superchat-workspace-id': '4c74be37-7615-4281-99a1-bfe6dfb47be4',
}

params_messages = {
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

page = 0
for conversation in ConversationData.objects.filter(status='New'):
    time.sleep(0.5)
    response_messages = requests.get(
        f'https://api.superchat.de/v9/conversations/{conversation.conversation_id}/timeline',
        headers=headers,
        params=params_messages
    )

    if response_messages.status_code == 200:                             
        messages_json = json.dumps(response_messages.json()['items'])
            
        conversation.messages_json = messages_json
        conversation.save()
        
        print(f"Conversation {conversation.conversation_id} updated")
    
    else:
        print(f"Request failed with status code: {response_messages.status_code}")
        print("Response text:", response_messages.text)