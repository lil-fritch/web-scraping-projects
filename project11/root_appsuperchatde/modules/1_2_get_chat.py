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
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlMta042TXRoT0t2WlFrNTdtM1ZWVyJ9.eyJodHRwczovL3N1cGVyY2hhdC5kZS9yb2xlIjoic3VwZXJ2aXNvciIsImh0dHBzOi8vc3VwZXJjaGF0LmRlL2xhbmd1YWdlIjoiZW4iLCJodHRwczovL3N1cGVyY2hhdC5kZS9wdWJsaWNVc2VySWQiOiJ1c19GNmtVTGREWEpnMHNWeE04anhDcEgiLCJodHRwczovL3N1cGVyY2hhdC5kZS9nbG9iYWxXb3Jrc3BhY2VJZCI6IjRjNzRiZTM3LTc2MTUtNDI4MS05OWExLWJmZTZkZmI0N2JlNCIsImh0dHBzOi8vc3VwZXJjaGF0LmRlL2lzU3VwZXJBZG1pbiI6bnVsbCwiaHR0cHM6Ly9zdXBlcmNoYXQuZGUvd29ya3NwYWNlU291cmNlIjoiUkVUT09MX1NBTEVTIiwiaHR0cHM6Ly9zdXBlcmNoYXQuZGUvcHVibGljVXNlckxvZ2luSWQiOiJ1c2xfOUZSR1RabUVjbXN4ZzZadWtXMm9TIiwiaXNzIjoiaHR0cHM6Ly9hdXRoLnN1cGVyY2hhdC5kZS8iLCJzdWIiOiJhdXRoMHw2NzI0ZDA0MzU1NDgzYzllMmY3NmVkZWMiLCJhdWQiOlsiaHR0cHM6Ly9hcGkuc3VwZXJjaGF0LmRlL2NvbnZlcnNhdGlvbi1zZXJ2aWNlIiwiaHR0cHM6Ly9zdXBlci1jaGF0LmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MzA3MDI0OTUsImV4cCI6MTczMDcxMTA5NSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBvZmZsaW5lX2FjY2VzcyIsImF6cCI6IkxRZHFGdGk2NHNyOWM5MkxhSldyVHpwNml6VDRiWmRnIn0.ZiW5z-bXR4Vqtrfoia0sBSUAVz0FoZ2m9q6mIqWVi43XN6RBeB8-EsqUhEzy6offfPl4VUnHq4I2w0EDUhGW8NQnfkLE_UuuZgOP7WNTx0Bemw-yLd1lNT9vPejhAsh46sfvS39fzbCQ7Xus1nVbJK9WCGPjAZPlzVsA7POdUQcrbBvmuoPQGHPsn-DXKQS6uAnRBAT0JEbDhCijeZXk4o7e0WGKV8V8bWlnkbk-MigFvXBaWE2YdvqzWeVD-MSO6RCc4XeOxKG_cJenM_QTSRmCnZo04IZRWEaQ6B38wGNIEUuv88BcfOASZT0tLIEaQZvnMus0B73qyKfsoiNl2A",
    "content-type": "application/json",
    "origin": "https://app.superchat.de",
    "referer": "https://app.superchat.de/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-superchat-platform": "WEB",
    "x-superchat-release-timestamp": "2024-10-31T16:16:47Z",
    "x-superchat-version": "c2f4e3fdb46b108f6d1e496f957ddf7ad7706834",
    "x-superchat-workspace-id": "4c74be37-7615-4281-99a1-bfe6dfb47be4",
}

# Parameters
params = {
    "inboxId": "ib_neMl63QAmdZKqRTDsPWTd",
    "status": "DONE",
    "sorting": "NEWEST",
    "page": 0  # Start with page 0
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

        conversations_list = data['items']
        for conversation in conversations_list:
            print()
            print('=' * 50)
            print(conversation)
            # with open('chat.json', 'w') as f:
            #     json.dump(conversation, f, indent=4)
            conv_id = conversation['id']
            print('ID: ', conv_id)

            link = 'https://app.superchat.de/inbox/' + conv_id
            print('Link: ', link)
            
            break
            # obj, created = Conversation.objects.get_or_create(
            #     conversation_id = conv_id,
            #     link = link,
            # )
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
