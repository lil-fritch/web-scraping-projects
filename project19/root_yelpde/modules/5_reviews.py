from load_django import *
from parser_app.models import *

import json

for item in Review.objects.filter(status='New'):
    json_data = json.loads(item.json_data)
    
    node = json_data['node']
    item.text = node.get('text', None)
    if item.text:
        item.language = item.text['language']
        item.text = item.text['full'].strip()
        
    
    item.created_at = node.get('createdAt')['localDateTimeForBusiness']
    item.rating = node.get('rating', None)
    author = node.get('author', None)
    item.author_id = author.get('encid', None)
    item.author_name = author.get('displayName', None)
    item.author_total_count_reviews = author.get('reviewCount', None)
    item.author_is_elite = bool(author.get('currentTruncatedEliteYear', None))
    
    reactions = node.get('availableReactionsContainer', None)['availableReactions']
    item.count_useful_reactions = reactions[0].get('count', None)
    item.count_thanks_reactions = reactions[1].get('count', None)
    item.count_love_this_reactions = reactions[2].get('count', None)
    item.count_oh_no_reactions = reactions[3].get('count', None)
    
    photos = []
    photos_data = node.get('businessPhotos', None)
    for photo_data in photos_data:
        photos.append(photo_data['viewerPhotoUrl']['url'])
    item.photos = photos
    
    item.status = 'Done'
    item.save()
    
    print(item, 'Done')
    