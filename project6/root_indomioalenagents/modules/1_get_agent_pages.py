'''
Walks through the saved countries 
and collects links to agent pages with detailed information
'''

import time
import requests
from bs4 import BeautifulSoup

from load_django import *
from parser_app.models import *

cookies = {
    'currency': 'eyJpdiI6IlwvQzNDN2pEZTVybEJsaUpFM0FuQXhRPT0iLCJ2YWx1ZSI6IjZPeDR0RzRiMHdrbElDTWY4NnA4TWQ0YWNtYVJaZVwvQkNqMjFwcm9Jb2VaeW5WM1ZvWEI4ZjFTODN0XC9NWVwvMzRWUkhaWFlqN3VsbnpWczAzVEcrXC84QmJjY0pyRTRLTFFvTTF0bTJjMTA0dz0iLCJtYWMiOiI1MmE3N2E1NjlhMTc5ODAyN2I0ZjRmYzNlZjNjZmRjZjgzMWU2NDNjOTU4OGYzOGUxMzRmZWY1MWRjODg5ZDhjIn0%3D',
    '_gid': 'GA1.2.1701798037.1730124473',
    '_oid': 'b7c16feb-e662-4c91-9ae6-431a449066c9',
    'panoramaId_expiry': '1730210875805',
    '_cc_id': '57e241a81fff08f4f2a69abd86e8831a',
    'panoramaId': 'aa4b67ca778d96a6c47970c541b2a9fb927a05f722423db2f1208ebb7108da65',
    'euconsent-v2': 'CQHQXcAQHQXcAAKA4AENBNFsAP_gAEPgAAyIKiNX_G__bWlr8X73aftkeY1P9_h77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIAu3TBIQNlGJDURVCgaogVryDMaEiUoTNKJ6BkiFMRM2dYCF5vm4tj-QCY5vr991dx2B-t7dr83dzyy41Hn3a5_2a0WJCdA5-tDfv9bROb-9IOd_x8v4v8_F_pE2_eT1l_tWvp7D9-cts7_XW89_fff_9Pn_-uB_-_3_vBUAAkw0KiAMsiQkINAwggQAqCsICKBAAAACQNEBACYMCnYGAS6wkQAgBQADBACAAEGQAIAABIAEIgAgAKBAABAIFAAEABAMBAAwMAAYALAQCAAEB0DFMCCAQLABIzIiFMCEIBIICWyoQSAIEFcIQizwKIBETBQAAAkAFYAAgLBYHEkgJWJBAlxBtAAAQAIBBAAUIpOzAEEAZstReLJtGVpgWD5gue0wDJAiAA.f_gAAAAAAAAA',
    'addtl_consent': '1~43.3.9.6.9.13.6.4.15.9.5.2.11.8.1.3.2.10.33.4.15.17.2.9.20.7.20.5.20.7.2.2.1.4.40.4.14.9.3.10.8.9.6.6.9.41.5.3.1.27.1.17.10.9.1.8.6.2.8.3.4.146.65.1.17.1.18.25.35.5.18.9.7.41.2.4.18.24.4.9.6.5.2.14.25.3.2.2.8.28.8.6.3.10.4.20.2.17.10.11.1.3.22.16.2.6.8.6.11.6.5.33.11.8.11.28.12.1.5.2.17.9.6.40.17.4.9.15.8.7.3.12.7.2.4.1.7.12.13.22.13.2.6.8.10.1.4.15.2.4.9.4.5.4.7.13.5.15.17.4.14.10.15.2.5.6.2.2.1.2.14.7.4.8.2.9.10.18.12.13.2.18.1.1.3.1.1.9.7.2.16.5.19.8.4.8.5.4.8.4.4.2.14.2.13.4.2.6.9.6.3.2.2.3.7.3.6.10.11.6.3.19.8.3.3.1.2.3.9.19.26.3.10.13.4.3.4.6.3.3.3.4.1.1.6.11.4.1.11.6.1.10.13.3.2.2.4.3.2.2.7.15.7.14.4.3.4.5.4.3.2.2.5.5.3.9.7.9.1.5.3.7.10.11.1.3.1.1.2.1.3.2.6.1.12.8.1.3.1.1.2.2.7.7.1.4.3.6.1.2.1.4.1.1.4.1.1.2.1.8.1.7.4.3.3.3.5.3.15.1.15.10.28.1.2.2.12.3.4.1.6.3.4.7.1.3.1.4.1.5.3.1.3.4.1.5.2.3.1.2.2.6.2.1.2.2.2.4.1.1.1.2.2.1.1.1.1.2.1.1.1.2.2.1.1.2.1.2.1.7.1.7.1.1.1.1.2.1.4.2.1.1.9.1.6.2.1.6.2.3.2.1.1.1.2.5.2.4.1.1.2.2.1.1.7.1.2.2.1.2.1.2.3.1.1.2.4.1.1.1.6.3.6.4.5.9.1.2.3.1.4.3.2.2.3.1.1.1.1.12.1.3.1.1.2.2.1.6.3.3.5.2.7.1.1.2.5.1.9.5.1.3.1.8.4.5.1.9.1.1.1.2.1.1.1.4.2.13.1.1.3.1.2.2.3.1.2.1.1.1.2.1.3.1.1.1.1.2.4.1.5.1.2.4.3.10.2.9.7.2.2.1.3.3.1.6.1.2.5.1.1.2.6.4.2.1.200.200.100.300.400.100.100.100.400.1700.304.596.100.1000.800.500.400.200.200.500.1300.801.99.506.95.1399.1100.100.4302.1798.2700.200.100.800.900.100.200.700.100.800.2000.900.1100.600.400.2200',
    'IABGPP_HDR_GppString': 'DBABMA~CQHQXcAQHQXcAAKA4AENBNFsAP_gAEPgAAyIKiNX_G__bWlr8X73aftkeY1P9_h77sQxBhfJE-4FzLvW_JwXx2ExNA36tqIKmRIAu3TBIQNlGJDURVCgaogVryDMaEiUoTNKJ6BkiFMRM2dYCF5vm4tj-QCY5vr991dx2B-t7dr83dzyy41Hn3a5_2a0WJCdA5-tDfv9bROb-9IOd_x8v4v8_F_pE2_eT1l_tWvp7D9-cts7_XW89_fff_9Pn_-uB_-_3_vBUAAkw0KiAMsiQkINAwggQAqCsICKBAAAACQNEBACYMCnYGAS6wkQAgBQADBACAAEGQAIAABIAEIgAgAKBAABAIFAAEABAMBAAwMAAYALAQCAAEB0DFMCCAQLABIzIiFMCEIBIICWyoQSAIEFcIQizwKIBETBQAAAkAFYAAgLBYHEkgJWJBAlxBtAAAQAIBBAAUIpOzAEEAZstReLJtGVpgWD5gue0wDJAiAA.f_gAAAAAAAAA',
    '_ga_TJZEPZL56H': 'GS1.1.1730207718.5.1.1730208171.59.0.0',
    '_ga': 'GA1.1.1777153718.1730124473',
    'XSRF-TOKEN': 'eyJpdiI6IjdNc2ZVMUFVNDY1TEtcL2JZaTdiYTN3PT0iLCJ2YWx1ZSI6InduWHVJTzhhVDl2bFd0aUhQaFI0WXhCaTVHMUdwcjBGaHM0ZTdRQmU5TTBJXC80MGpacFprS1JwMGU1bTA4dTd1eUttbmh4Q3FWZU8zbnlWaTdNY0RBZz09IiwibWFjIjoiYjYyMWI0M2IwOTE5ZTYxM2RhNThhMmY5YmI3Y2Q1ZTkxOWJmNGYxMjdlOWM4YzJlNzFkNGY4MDEzYTkxNGVhNiJ9',
    'laravel_session': 'eyJpdiI6IllXRHM1QXFXXC9sOVFnbDI3azhvQmxnPT0iLCJ2YWx1ZSI6InNpaU5vdUk1RlwvSXZHdlJvN1B0Y2Voam5IaUVSZ0cxXC9wUzh4WGVYNTY4aUxWQUZhU3Ywcnl4VzFzSDVKZHFJbUhlS21WRTYzRVJBSm1XV25yXC95UHVBPT0iLCJtYWMiOiI1MTU2NmI1YWEyN2MzNGIxZDBjY2JkNjQzYmYyZTVkMGU5NmZhMDk5ZjA2ZWZhMTMxYmE4MDUzMGIxM2M0ZTA1In0%3D',
    'cto_bundle': 'EFmlNV9FUElpNGhkSTlxSmJ4QllJUjFxb2NNajhwOE9EMXVvVThtUU5ZZkdSVVFVYU8wdFhtUUFCSHJzelpjcHFKT1Bhbm5nRG9QVUIlMkYyMWJKWW9uTThLd2VuVmJsMWM4SVhsY0h3WmtBaXNzdUIlMkIxMDhtanE1SEJLNCUyRkhBNURNNFVodW9lTW8lMkZ6dlkzckxIRlFhTGZ5eEFLZyUzRCUzRA',
    'cto_bidid': 'dWOQ119kM0NNb3dCRFpmNW84amM5VCUyRmFvNjZyJTJGcHFGNGQ1V00lMkJQV3VvSyUyRkRydnp0ZnJONGRWQmtGbktCZ3NySnNDMVFWU1Z5d1BObSUyQk0yWGNxUjlRM3BDekNFWVpxaE81M3Vub0x0YkhiUGF0S1klM0Q',
    'reese84': '3:XfuEw9P/JHTKOIvBJQZ19g==:mGf3MMNSN+ZGttuAACNtt0I2YKV/1B6hlIibQ6G6xVz8S1fxIQFo+/agorZsNgw8rnEntU2jreTd8VHQTiK1nYdpAyzKZmIiFTjKGdRA1kQFEMZ516RL9wg9U9/Yma6QLMFCk4dubbM88rS3slHIUwDnmwisYSLvi+Iu6tTSIsZ6TAwhwH+uCCMMFSM1rh3nlWbUTe8gpbjNRk/8y8kpXjxAELJmA7ejdVF4lPRkkF1FabTz3n+2JTXG4udG1TVZDLgx5B4vDjmPLIMj6VTvZpH9fvQ3oMiXfWmXmoPItgeOq3RnSvzi9bKWRe9CTFrElRPkWn9mMfxQ2tOMAYi/Hs9jlBLjcgKkAx62P6HmaTV4/E4Ojs08coLO089RiS9xQhYKRYMHrbHpYjhCZCgzdD9NI+hV3CL1lbeaIrdzktSxB0MrH8Qa9/E04FLpJ8F1nFY+eOHaiDFxlcoz/Vae0Q==:/brBpe/x8Zx3Xtm2mxfpsIMH5kiN4XR3luoEmRxtQU4=',
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

url = 'https://www.indomio.al/en/agents'

for country in Country.objects.filter(status='New').order_by('id'):
    stop = False

    for page in range(1, 100000):

        respone = requests.get(f'{country.url}?page={page}', headers=headers, cookies=cookies)

        time.sleep(2)
        print(f'Country: {country.name} Page: {page}')

        if respone.status_code == 200:
            if 'Nothing found' in respone.text:
                print('Nothing found')
                break
            
            soup = BeautifulSoup(respone.text, 'html.parser')
            
            all_agent_links = soup.find_all('a', class_='agentEntry__logo')
            if not all_agent_links:
                continue
                
            for agent_link in all_agent_links:
                
                agent_url = agent_link['href']
                
                item, created = Page.objects.get_or_create(
                    url=agent_url
                )
                print(f'{created} - {item}')
        
        elif respone.status_code == 405 or respone.status_code == 403:
            print('Site is blocked. Change cookies')
            stop = True
            break
        else:
            print(f'Error: {respone.status_code}')
    
    if stop:
        break
    
    country.status = 'Done'
    country.save()
    