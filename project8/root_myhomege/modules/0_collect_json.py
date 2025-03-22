import json
import requests

from load_django import *
from parser_app.models import *
    
url = "https://www.myhome.ge/block/getJSON.php"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://www.myhome.ge",
    "Referer": "https://www.myhome.ge/ka/maklers/?makler_type_id=1&page=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

payload = {
    "do": "makler_search",
    "q": "",
    "makler_type_id": "1",
    "page": "1"
}

cookies = {
    "PHPSESSID": "37nlf05ntf86k6oprghe5allk2",
    "split_test": "v1",
    "_gcl_au": "1.1.1264604303.1730286381",
    "_ga": "GA1.1.204495870.1730286381",
    "_clck": "1lttnlo|2|fqg|0|1764",
    "cardView": "2",
    "_clsk": "1vwxumf|1730286408146|2|1|v.clarity.ms/collect",
    "_ga_B3H1RB8TBF": "GS1.1.1730286381.1.1.1730286418.23.0.0",
    "_ga_R5Q4Z312FE": "GS1.1.1730286381.1.1.1730286418.23.0.1820739106",
    "_ga_95XZDEWDK1": "GS1.1.1730286382.1.1.1730286418.24.0.0"
}

for page in range(1, 10000):
    print("Page: " + str(page))
    payload["page"] = str(page)
    
    response = requests.post(url, headers=headers, data=payload, cookies=cookies)
    
    json_data = response.json()
    
    try:
        result = json_data['result']
    except:
        print('No result')
        break

    for item in result:
        
        agency_and_agent_data = (result[item])
                
        for agent in agency_and_agent_data['agents']:
            
            agent_id = agent['user_id']
            
            agent_json_data = json.dumps(agent)
            agency_json_data = json.dumps(agency_and_agent_data['makler'])
            
            item, created = Agent.objects.get_or_create(
                agent_id = agent_id,
                agent_json = agent_json_data,
                agency_json = agency_json_data
            )
            print(created, item)

            