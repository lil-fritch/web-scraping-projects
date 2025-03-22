'''
Goes through the saved agents and collects their email addresses.
'''

from concurrent import futures
from load_django import *
from parser_app.models import Agent

from bs4 import BeautifulSoup
import requests

headers = {
    'Referer': 'https://www.myhome.ie/estate-agents/page-1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

items = Agent.objects.filter(status="Done")
# for item in items:
def main(item):
    if item.email:
        return
    url = item.url
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        email_element = soup.find('svg', class_='svg-inline--fa fa-envelope')
        try:
            email = email_element.parent.parent.text.strip()
        except AttributeError:
            email = None
        item.email = email
        item.save()
        print(f"Email for {item}: {email}")

with futures.ThreadPoolExecutor(10) as executor:
    executor.map(main, items)
