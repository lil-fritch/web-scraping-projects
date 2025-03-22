from load_django import *
from parser_app.models import *

from search_companies import GoogleMapsScraper

# class GetLinks:
#     def __init__(self):
#         self.scraper = GoogleMapsScraper()

#     def get_links(self, items):
#         for item in items:
#             response = self.scraper.scrape_link(item.link)

#             for link, name in response:
#                 obj, created = Link.objects.get_or_create(
#                     country=item.country,
#                     city=item.city,
#                     state=item.state,
#                     zip_code=item.zip_code,
#                     category=item.category,
#                     keyword=item.name,
#                     name=name,
#                     link=link,
#                 )
#                 print(created, obj)
#             print(len(response))
#             item.status = 'Done'
#             item.save()


# get_links = GetLinks(scraper)
# get_links.get_links(Keyword.objects.filter(status='New'))

scraper = GoogleMapsScraper()   
# test='https://www.google.com.ua/maps/search/urgent+cares+near+56567+mn+usa/@45.7081451,-95.5834935,8z/data=!3m1!4b1?hl=en&entry=ttu&g_ep=EgoyMDI0MTExMy4xIKXMDSoASAFQAw%3D%3D'
for item in Keyword.objects.filter(status='New'):
    respone = scraper.scrape_link(item.link)
    
    for name, link in respone.items():
        obj, created = Link.objects.get_or_create(
            link=link,
            defaults={
                'country': item.country,
                'city': item.city,
                'state': item.state,
                'zip_code': item.zip_code,
                'category': item.category,
                'keyword': item.name,
                'name': name,
            }
        )
        print(created, obj)
    print(len(respone))
    item.status = 'Done'
    item.save()