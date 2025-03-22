'''
Collects all agencies by going through the search pages 
for further collection of agents
'''

from bs4 import BeautifulSoup
import requests

from load_django import *
from parser_app.models import *

cookies = {
    'SLINGSHOT': 'LanguageCode=he-IL',
    'SessionId': '',
    'ASP.NET_SessionId': 'duykmlbe052fh1554d011yxw',
    'SelectedModeCookie': 'residential',
    '_gcl_au': '1.1.1712061631.1731080166',
    '_gid': 'GA1.2.1948804951.1731080167',
    '__utmc': '136538803',
    '__utmz': '136538803.1731080204.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utma': '136538803.1647375933.1731080167.1731080204.1731083242.2',
    '__utmt': '1',
    '_gat_UA-1993435-2': '1',
    '__utmb': '136538803.5.10.1731083242',
    'clix.session': '3862207844058450',
    '_ga_MKYRY78B5M': 'GS1.1.1731083241.2.1.1731083747.31.0.0',
    '_ga': 'GA1.1.1647375933.1731080167',
}

headers = {
    'accept': '*/*',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://www.remax-israel.com/officeagentsearch.aspx',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'mode': 'list',
    'type': '1',
    'regionId': '5',
    'regionRowId': '',
    'provinceId': '',
    'cityId': '',
    'localzoneId': '',
    'name': '',
    'location': '',
    'spokenLanguageCode': '',
    'page': '1',
    'countryCode': 'HE',
    'countryEnuName': 'Israel',
    'countryName': 'Israel',
    'selmode': 'residential',
    'officeId': '',
    'macroOfficeId': '',
    'selectedCountryID': '',
    'initialRegionId': '5',
    'defaultRegionRowId': '',
    'defaultProvinceId': '',
    'defaultLocation': '',
}

for page in range(1, 100):
    params['page'] = page
    response = requests.get(
        'https://www.remax-israel.com/handlers/officeagentsearch.ashx',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        agencies = soup.find_all('div', class_='list-result')
        if len(agencies) == 0:
            break
        for agency_data in agencies:
            try:
                agency_url = agency_data.find('a', class_='office-name')['href']
            except AttributeError:
                agency_url = None
            try:
                agency_office_fax = agency_data.find('p', id='office-fax').text.strip()
            except AttributeError:
                agency_office_fax = None

            item, created = Agency.objects.get_or_create(url=agency_url, office_fax=agency_office_fax)
            print(created, item)
    else:
        print('Error', response.status_code)