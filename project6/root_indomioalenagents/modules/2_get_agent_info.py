'''
Goes through the saved agent pages 
and saves information about them to the database
'''

import base64
from concurrent import futures
import random
import time
import requests
from bs4 import BeautifulSoup

from load_django import *
from parser_app.models import *

cookies = {
    'currency': 'eyJpdiI6IlwvQzNDN2pEZTVybEJsaUpFM0FuQXhRPT0iLCJ2YWx1ZSI6IjZPeDR0RzRiMHdrbElDTWY4NnA4TWQ0YWNtYVJaZVwvQkNqMjFwcm9Jb2VaeW5WM1ZvWEI4ZjFTODN0XC9NWVwvMzRWUkhaWFlqN3VsbnpWczAzVEcrXC84QmJjY0pyRTRLTFFvTTF0bTJjMTA0dz0iLCJtYWMiOiI1MmE3N2E1NjlhMTc5ODAyN2I0ZjRmYzNlZjNjZmRjZjgzMWU2NDNjOTU4OGYzOGUxMzRmZWY1MWRjODg5ZDhjIn0%3D',
    '_gid': 'GA1.2.1701798037.1730124473',
    '_oid': 'b7c16feb-e662-4c91-9ae6-431a449066c9',
    '_cc_id': '57e241a81fff08f4f2a69abd86e8831a',
    'euconsent-v2': 'CQHQXcAQHQXcAAKA4AENBNFsAP_gAEPgAAyIKiNX_G__bWlr8X73aftkeY1P9_h77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIAu3TBIQNlGJDURVCgaogVryDMaEiUoTNKJ6BkiFMRM2dYCF5vm4tj-QCY5vr991dx2B-t7dr83dzyy41Hn3a5_2a0WJCdA5-tDfv9bROb-9IOd_x8v4v8_F_pE2_eT1l_tWvp7D9-cts7_XW89_fff_9Pn_-uB_-_3_vBUAAkw0KiAMsiQkINAwggQAqCsICKBAAAACQNEBACYMCnYGAS6wkQAgBQADBACAAEGQAIAABIAEIgAgAKBAABAIFAAEABAMBAAwMAAYALAQCAAEB0DFMCCAQLABIzIiFMCEIBIICWyoQSAIEFcIQizwKIBETBQAAAkAFYAAgLBYHEkgJWJBAlxBtAAAQAIBBAAUIpOzAEEAZstReLJtGVpgWD5gue0wDJAiAA.f_gAAAAAAAAA',
    'addtl_consent': '1~43.3.9.6.9.13.6.4.15.9.5.2.11.8.1.3.2.10.33.4.15.17.2.9.20.7.20.5.20.7.2.2.1.4.40.4.14.9.3.10.8.9.6.6.9.41.5.3.1.27.1.17.10.9.1.8.6.2.8.3.4.146.65.1.17.1.18.25.35.5.18.9.7.41.2.4.18.24.4.9.6.5.2.14.25.3.2.2.8.28.8.6.3.10.4.20.2.17.10.11.1.3.22.16.2.6.8.6.11.6.5.33.11.8.11.28.12.1.5.2.17.9.6.40.17.4.9.15.8.7.3.12.7.2.4.1.7.12.13.22.13.2.6.8.10.1.4.15.2.4.9.4.5.4.7.13.5.15.17.4.14.10.15.2.5.6.2.2.1.2.14.7.4.8.2.9.10.18.12.13.2.18.1.1.3.1.1.9.7.2.16.5.19.8.4.8.5.4.8.4.4.2.14.2.13.4.2.6.9.6.3.2.2.3.7.3.6.10.11.6.3.19.8.3.3.1.2.3.9.19.26.3.10.13.4.3.4.6.3.3.3.4.1.1.6.11.4.1.11.6.1.10.13.3.2.2.4.3.2.2.7.15.7.14.4.3.4.5.4.3.2.2.5.5.3.9.7.9.1.5.3.7.10.11.1.3.1.1.2.1.3.2.6.1.12.8.1.3.1.1.2.2.7.7.1.4.3.6.1.2.1.4.1.1.4.1.1.2.1.8.1.7.4.3.3.3.5.3.15.1.15.10.28.1.2.2.12.3.4.1.6.3.4.7.1.3.1.4.1.5.3.1.3.4.1.5.2.3.1.2.2.6.2.1.2.2.2.4.1.1.1.2.2.1.1.1.1.2.1.1.1.2.2.1.1.2.1.2.1.7.1.7.1.1.1.1.2.1.4.2.1.1.9.1.6.2.1.6.2.3.2.1.1.1.2.5.2.4.1.1.2.2.1.1.7.1.2.2.1.2.1.2.3.1.1.2.4.1.1.1.6.3.6.4.5.9.1.2.3.1.4.3.2.2.3.1.1.1.1.12.1.3.1.1.2.2.1.6.3.3.5.2.7.1.1.2.5.1.9.5.1.3.1.8.4.5.1.9.1.1.1.2.1.1.1.4.2.13.1.1.3.1.2.2.3.1.2.1.1.1.2.1.3.1.1.1.1.2.4.1.5.1.2.4.3.10.2.9.7.2.2.1.3.3.1.6.1.2.5.1.1.2.6.4.2.1.200.200.100.300.400.100.100.100.400.1700.304.596.100.1000.800.500.400.200.200.500.1300.801.99.506.95.1399.1100.100.4302.1798.2700.200.100.800.900.100.200.700.100.800.2000.900.1100.600.400.2200',
    'IABGPP_HDR_GppString': 'DBABMA~CQHQXcAQHQXcAAKA4AENBNFsAP_gAEPgAAyIKiNX_G__bWlr8X73aftkeY1P9_h77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIAu3TBIQNlGJDURVCgaogVryDMaEiUoTNKJ6BkiFMRM2dYCF5vm4tj-QCY5vr991dx2B-t7dr83dzyy41Hn3a5_2a0WJCdA5-tDfv9bROb-9IOd_x8v4v8_F_pE2_eT1l_tWvp7D9-cts7_XW89_fff_9Pn_-uB_-_3_vBUAAkw0KiAMsiQkINAwggQAqCsICKBAAAACQNEBACYMCnYGAS6wkQAgBQADBACAAEGQAIAABIAEIgAgAKBAABAIFAAEABAMBAAwMAAYALAQCAAEB0DFMCCAQLABIzIiFMCEIBIICWyoQSAIEFcIQizwKIBETBQAAAkAFYAAgLBYHEkgJWJBAlxBtAAAQAIBBAAUIpOzAEEAZstReLJtGVpgWD5gue0wDJAiAA.f_gAAAAAAAAA',
    'panoramaId_expiry': '1730298390309',
    'panoramaId': 'aa4b67ca778d96a6c47970c541b2a9fb927a05f722423db2f1208ebb7108da65',
    '_ga': 'GA1.1.1777153718.1730124473',
    '_ga_TJZEPZL56H': 'GS1.1.1730219142.7.1.1730219660.60.0.0',
    'XSRF-TOKEN': 'eyJpdiI6IjdvaVRUOEQ3SE5UNHJxeGowbEUzN3c9PSIsInZhbHVlIjoiMGxIUSswREp6bmlCWkVpRFJ0QTF3cEh2R2l2cEVcL2M1Q2ZmbWJRT2piNFEwNTJLU1pOT2lqUmRmQnNraERjc1wvektMZlc4R2JzZEwralNRTWpCeUFaUT09IiwibWFjIjoiZmNiZjlhOWQ1YzZkYTY2ZTk3NTdiZTM0MmJkMmU1N2Q5N2QxNzEwYzBjNzFhZjUxMjIxOWJlYjcwZDEwNzYwNSJ9',
    'laravel_session': 'eyJpdiI6IkduNTlRTit0T2o0OVpCRzBPa01DYUE9PSIsInZhbHVlIjoiWmNaSzk5OERGYUozRVFQM0JrMUNrWjh1S1BXNEFjU3lFRTJuSEJBUGRyeTFhOUpTSGZsYUpFaGJvVkEyRWlhQzVXeEhhS1E3dGh2ZUtOQnZ1eXlYSHc9PSIsIm1hYyI6IjlmZDQyNzc0ZWE4YmIwYWYxYzAxMjhhNTFmNzU5ODdiZTg0ZGFhN2UwMWY5YWEwZjMyNGExYzYyODZhY2MxNjcifQ%3D%3D',
    'cto_bundle': 'gdAQml9FUElpNGhkSTlxSmJ4QllJUjFxb2NJJTJCejF0WWp4bmpUWXVMUWlISkQxSmJ5SjJscnVXVjN5UWVtanNsVGt5JTJCaWMxeGFhc1d3NkpXeTNpMGxnRk5MZ2VCbzlPVld2Y2l3QVJib2h0aU9aeFdDcWx5RVBaWDJwSWFxN0ZCek1MZjRocyUyRjVlZGFaNk5WRzh3R0NyVG54VFElM0QlM0Q',
    'cto_bidid': 'qA38A19kM0NNb3dCRFpmNW84amM5VCUyRmFvNjZyJTJGcHFGNGQ1V00lMkJQV3VvSyUyRkRydnp0ZnJONGRWQmtGbktCZ3NySnNDMVFWU1Z5d1BObSUyQk0yWGNxUjlRM3BDek55QXc3cGZFTTRaU0haUGt3QjE3MWclM0Q',
    'reese84': '3:LxeUu0qyq2bfDpw+4Q2UMg==:0Ltb1Kti+NOONkbA4LaYQNdPa046ipsizkUTbT13lNbqntmZ6GPcNeArpsyZ9WyeoxNT5R0AbbuMiI1gu8WM9rQVwU7FIqKEEa6XRtVxq87gplNSM70KN4FXznVB++Y+PwtSdle9wQWsgv3cD3jFQXp4dQNF9xcpn9ZzYcP4IQW9jZ4sbUf8EYUDlB8XRnoxJw0Z6eeFPKGlVe2Adw/jn1mc/bAy3sQ6ny7a0E1tc/5HeKWGT4i9YuT/sbzX55YrSgPD1lP/KNf2RGQQk1+pij7G8HoDnD52r5Us9u0eHF9X51Ag/PK8C6NYTlXK8wXC9O0BX9IDqphFWygjNor+lZttckYbxWTwiZLFxHT1oLnvnUeq0YUrgZaJ3BxDXJhfeSLhoDOJQljIBkJfi0kRQtL64suOfQMUKxnHeDkeOOvwjfSFEDMYrvevXKUi8fBZRiFYlUdpMZpbZCFKp1/Hzsb/WUOI+eOIfPoWJ87/mNT7RqEpYw5Nk89Mla3wxkwD:vaDR3ZVpHOXawjWN6rrzO761Hj6m4Q8LdVNVg29T2VE=',
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

agent = {}
for page in Page.objects.filter(status="New"):
# def main(page):
    time.sleep(random.randint(1, 3))

    respone = requests.get(page.url, headers=headers, cookies=cookies)
    
    if respone.status_code == 200:
        soup = BeautifulSoup(respone.text, 'html.parser')
        agent_info_block = soup.find('div', class_='agent-info-cont')
        
        if not agent_info_block:
            print('No agent info block')
            continue
        
        agent['url'] = page.url

        try:
            agent['title'] = agent_info_block.find('h1', class_='agent-info__title').text.strip()
        except AttributeError:
            agent['title'] = None
        try:
            agent['name'] = agent_info_block.find('span', class_='agent-info__el agent-info__el--name').text.strip()
        except AttributeError:
            agent['name'] = None
        try:
            phones = []
            phone_block = agent_info_block.find('span', class_='agent-info__el agent-info__el--phone').find('span', class_='hidden')
            encoded_phone_elements = phone_block.find_all('a')
            for encoded_phone_element in encoded_phone_elements:
                encoded_phone = encoded_phone_element.text
                phone = base64.b64decode(encoded_phone).decode('utf-8')
                phones.append(phone)
            agent['phones'] = phones.copy()
            phones.clear()
        except AttributeError:
            agent['phones'] = None
        try:
            agent['address'] = agent_info_block.find('span', class_='agent-info__el agent-info__el--location').text.strip()
            agent['address'] = " ".join(agent['address'].split())
        except AttributeError:
            agent['address'] = None
        try:
            agent['website'] = agent_info_block.find('a', class_='ext-link')
            if agent['website']:
                agent['website'] = agent['website']['href']
            else:
                agent['website'] = None
        except AttributeError:
            agent['website'] = None
        try:
            agent['facebook'] = agent_info_block.find('i', class_='fa fa-facebook')
            if agent['facebook'] and agent['facebook'].parent.name == 'a':
                agent['facebook'] = agent['facebook'].parent['href']
            else:
                agent['facebook'] = None
        except AttributeError:
            agent['facebook'] = None
        try:
            agent['instagram'] = agent_info_block.find('i', class_='fa fa-instagram')
            if agent['instagram'] and agent['instagram'].parent.name == 'a':
                agent['instagram'] = agent['instagram'].parent['href']
            else:
                agent['instagram'] = None
        except AttributeError:
            agent['instagram'] = None
        try:
            agent['youtube'] = agent_info_block.find('i', class_='fa fa-youtube')
            if agent['youtube'] and agent['youtube'].parent.name == 'a':
                agent['youtube'] = agent['youtube'].parent['href']
            else:
                agent['youtube'] = None
        except AttributeError:
            agent['youtube'] = None
        try:
            agent['linkedin'] = agent_info_block.find('i', class_='fa fa-linkedin')
            if agent['linkedin'] and agent['linkedin'].parent.name == 'a':
                agent['linkedin'] = agent['linkedin'].parent['href']
            else:
                agent['linkedin'] = None
        except AttributeError:
            agent['linkedin'] = None
        try:
            agent['logo'] = agent_info_block.find('div', class_='agent-logo').find('img')
            if agent['logo']:
                agent['logo'] = agent['logo']['src']
            else:
                agent['logo'] = None
        except AttributeError:
            agent['logo'] = None
        try:
            banner = soup.find('div', class_='agent-info-cont')
            if banner:
                style = banner.get('style')
                agent['banner'] = style.split('url(')[1].split(')')[0] if 'url(' in style else None
            else:
                agent['banner'] = None
        except AttributeError:
            agent['banner'] = None
        
        if sum(1 for value in agent.values() if value) < 2:
            print('No data')
            continue
        
        item, created = Agent.objects.get_or_create(
            url = agent['url'],
            defaults=agent
        )
        print(f'{created}: {item}')
        
        page.status = 'Done'
        page.save()
    else:
        print(f'Error {respone.status_code}')

# pages = Page.objects.filter(status="New").order_by('id')
# with futures.ThreadPoolExecutor(5) as executor:
    # executor.map(main, pages)
