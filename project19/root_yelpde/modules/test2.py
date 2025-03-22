from load_django import *
from parser_app.models import *
import csv

# items = Business.objects.filter(description__isnull=False).order_by('id')
# print(items.count())
# for item in items:
#     item.description = None
#     item.rewritten_description = None
#     item.save()
#     print(item, 'Done')
    
# items = Business.objects.filter(description_2__isnull=False).order_by('id')
# print(items.count())
# for item in items:
#     item.description = item.description_2
#     item.rewritten_description = item.rewritten_description_2
#     print(item, 'Done')
#     item.save()

items = SearchWitoutCategory.objects.filter(status='New').order_by('id')
count = 0
for item in items:
    if count == 3000:
        break   
    item.status = 'Done'
    item.save()
    count += 1

    
    # if item.logo_url == item.photo_url or item.logo_url == 'https://s3-media4.fl.yelpcdn.com/bphoto/3M89HndF9SYSQIk66CZVnA/l.jpg':
    #     item.logo_url = None
    #     item.save()
    #     print(item, 'Done')
        