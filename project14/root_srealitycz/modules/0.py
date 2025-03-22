import requests
from bs4 import BeautifulSoup

from load_django import *
from parser_app.models import *

for page in range(1, 500):
    respone = requests.get(f'https://www.sreality.cz/adresar?strana={page}')
    if respone.status_code == 200:
        soup = BeautifulSoup(respone.text, 'html.parser')
        agencies = soup.find_all('a', class_='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways css-vpeef3')
        if len(agencies) == 0:
            break
        for agency in agencies:
            url = 'https://www.sreality.cz'+agency['href']

            item, created = Agency.objects.get_or_create(url=url)
            print(created, item)
            
    else:
        print(f"Failed to fetch page {page}, status code: {respone.status_code}")