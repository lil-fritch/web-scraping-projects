'''
Enters all the letters of the alphabet one by one in the search bar 
and collects information about vets.
'''

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

from bs4 import BeautifulSoup

import time

from load_django import *
from app.models import *

URL = 'https://vetboard.vic.gov.au/VPRBV/VPRBV/VetSearch.aspx?hkey=ff033a35-97fd-4bdd-a9a4-ebaa0b125b7b'

cookies = {
    'ASP.NET_SessionId': '3czr4wjek1zxpxw5nctkelxu',
    '__RequestVerificationToken': 'mgk7aJKlP-Q-HE6VAb0R0o9f-aIjGpO2j7VG4D6oc0AI_RNt_pWKJrzQZGaTeo8Nj7Ml8vT56ZEc5ehY2wPdyWwyudsrw5PGaohELCKqK9A1',
    '_ga': 'GA1.4.1313079921.1729771054',
    '_gid': 'GA1.4.1755840378.1729771054',
    '_gat': '1',
    '_ga_NKVSHV4HXB': 'GS1.4.1729778877.3.0.1729778877.0.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)

vet = {}
for s in alphabet:
    
    search_box = driver.find_element(By.NAME, 'ctl01$TemplateBody$WebPartManager1$gwpciNewQueryMenuCommon$ciNewQueryMenuCommon$ResultsGrid$Sheet0$Input0$TextBox1')
    
    search_box.send_keys(Keys.BACKSPACE)
    search_box.send_keys(s)

    time.sleep(1)
    send_button = driver.find_element(By.NAME, 'ctl01$TemplateBody$WebPartManager1$gwpciNewQueryMenuCommon$ciNewQueryMenuCommon$ResultsGrid$Sheet0$SubmitButton')
    send_button.send_keys(Keys.RETURN)
    
    time.sleep(10)    
    
    for current_page in range(1, 1000):
        
        print('#'*20)
        print(f'Search: {s} Page: {current_page}')
        print('#'*20)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
                    
        all_vets_info = soup.find_all('tr', class_=['rgRow', 'rgAltRow'])
        for vet_info in all_vets_info:
            if not vet_info.text.strip():
                continue
            try:
                vet['name'] = vet_info.find('strong').text.strip()
            except AttributeError:
                vet['name'] = None
            try:
                vet['address'] = vet_info.find_all('td')[1].text.strip()
                if not vet['address']:
                    vet['address'] = None
            except AttributeError:
                vet['address'] = None
            try:
                vet['status'] = vet_info.find_all('td')[2].contents[0].strip()
            except AttributeError:
                vet['status'] = None
            try:
                vet['registration_no'] = vet_info.find('em').next_sibling.strip()
            except AttributeError:
                vet['registration_no'] = None
            try:
                vet['endorsed_in'] = vet_info.find_all('td')[3].text.replace('Endorsed in:', '').strip()
                if vet['endorsed_in'] == '':
                    vet['endorsed_in'] = None
            except AttributeError:
                vet['endorsed_in'] = None

            item, created = Vet.objects.get_or_create(
                name=vet['name'],
                address=vet['address'],
                status=vet['status'],
                registration_no=vet['registration_no'],
                endorsed_in=vet['endorsed_in']
            )
            print(created, item)
        
        if current_page % 10 == 0:
            try:
                next_page_button = driver.find_element(By.XPATH, "//a[contains(@title, 'Next Pages')]")
            except NoSuchElementException:
                break
        else:
            next_page_buttons = driver.find_elements(By.XPATH, "//a[contains(@title, 'Go to Page')]")
            for button in next_page_buttons:
                if button.text == str(current_page+1):
                    next_page_button = button
        try:
            next_page_button.click()
        except StaleElementReferenceException:
            print('No more pages')
            break   

        time.sleep(2)        
        
driver.quit()