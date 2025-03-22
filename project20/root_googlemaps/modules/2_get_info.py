import json
import re
from time import sleep

from load_django import *
from parser_app.models import *

from selenium_launcher import SeleniumDriver

from company_info import GoogleMapsScraper
from about import AboutCollector
from review import ReviewCollector

driver = SeleniumDriver()

scraper = GoogleMapsScraper(driver.get_driver())
about_collector = AboutCollector(driver.get_driver())
review_collector = ReviewCollector(driver.get_driver())

pattern = r"!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)"

try:
    for item in Link.objects.filter(status='New'):
        print('\n'+item.link)

        driver.load_url(item.link)
        overview = scraper.get_overview()
        sleep(1) 
        # about_info = about_collector.collect_about()
        # reviews = review_collector.collect_reviews()

        match = re.search(pattern, item.link)
        if match:
            latitude = float(match.group(1))
            longitude = float(match.group(2))

        obj, created = Place.objects.get_or_create(
            link = item.link,
            defaults={
                'category': item.category,
                'keyword': item.keyword,
                'name': overview.get('name'),
                'rating': overview.get('rating'),
                'num_reviews': overview.get('num_reviews'),
                # 'reviews_list': reviews,
                # 'about': about_info,
                'full_address': overview.get('full_address'),
                'country': overview.get('country'),
                'city': overview.get('city'),
                'state': overview.get('state'),
                'zip_code': overview.get('zip_code'),
                'address': overview.get('address'),
                'located_in': overview.get('located_in'),
                'lat': latitude,
                'lng': longitude,
                'place_type': overview.get('place_type'),
                'open_hours': overview.get('open_hours'),
                'open_24_7': overview.get('open_24_7'),
                'phone': overview.get('phone'),
                'website': overview.get('website'),
            }
            # category=item.category,
            # keyword=item.keyword,
            
            # name=overview.get('name'),
            
            # rating=overview.get('rating'),
            # num_reviews=overview.get('num_reviews'),
            # # reviews_list=reviews,
            
            # # about=about_info,
            
            # full_address=overview.get('full_address'),
            # country=overview.get('country'),
            # city=overview.get('city'),
            # state=overview.get('state'),
            # zip_code=overview.get('zip_code'),
            # address=overview.get('address'),
            # located_in=overview.get('located_in'),
            # lat = latitude,
            # lng = longitude,
            
            # place_type=overview.get('place_type'),
            # open_hours=overview.get('open_hours'),
            # open_24_7=overview.get('open_24_7'),
            
            # phone=overview.get('phone'),
            # website=overview.get('website'),
            
            # link = item.link,
        )
        print(created, obj)
        
        item.status = 'Done'
        item.save()
            
finally:
    driver.quit()