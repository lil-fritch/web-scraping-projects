from load_django import *
from parser_app.models import *

import requests

cookies = {
    'bse': '9ef7a45dc15d4fd7a72547df4ea2e2c8',
    'wdi': '2|04DC3DF4D80D13E3|0x1.9ce28ff43e319p+30|23162519e106c815',
    'xcj': '1|dvN39xdxRj5-jSRnVMcLWwRwSY1m3CCBTHzCpopz9-E',
    'datadome': 'cTaLgyh022k9ZYmTJRe_tRTk9hgOnSQJNTHF43nhXdhf_yp~ZKKdM7M~1CZvTAJdf4hoxO7xWmFpJGx04z5ikPDGuswMbFcPpoFFihpN2zAgJ1g880QWgBl0ghOpV15I',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'uk-UA,uk;q=0.9',
    'content-type': 'application/json',
    # 'cookie': 'bse=9ef7a45dc15d4fd7a72547df4ea2e2c8; wdi=2|04DC3DF4D80D13E3|0x1.9ce28ff43e319p+30|23162519e106c815; xcj=1|dvN39xdxRj5-jSRnVMcLWwRwSY1m3CCBTHzCpopz9-E; datadome=cTaLgyh022k9ZYmTJRe_tRTk9hgOnSQJNTHF43nhXdhf_yp~ZKKdM7M~1CZvTAJdf4hoxO7xWmFpJGx04z5ikPDGuswMbFcPpoFFihpN2zAgJ1g880QWgBl0ghOpV15I',
    'priority': 'u=1, i',
    'referer': 'https://www.yelp.de/biz/morrison-atwater-village-los-angeles?osq=Restaurants',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# statuses = ['FullDescription', 'DoneRewriteDescription']
statuses = ['DoneLogo']

for business in Business.objects.filter(status__in=statuses).order_by('id'):
    response = requests.get(f'https://www.yelp.de/biz/{business.business_id}/props', cookies=cookies, headers=headers)
    if response.status_code == 200:
        data = response.json()['bizDetailsPageProps']['businessPostsCarouselProps']['businessAvatar']
        business.logo_url = data['urlPrefix'] + 'ls' + data['urlSuffix']
        if not 'businessregularlogo' in business.logo_url:
            business.logo_url = None
        business.status = 'DoneLogo'
        business.save()
        print(business, 'DoneLogo')
    else:
        print('Error', response.status_code)