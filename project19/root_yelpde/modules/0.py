from load_django import *
from parser_app.models import *

import csv

indexes = []

with open('german-postcodes.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    
    for row in reader:
        plz = row['Plz']
        if plz:
            indexes.append(int(plz))
descs = [
    'Restaurants', 'Lieferservice', 'Zum Abholen',
    'Accountants', 'Plumbers', 'Autowerkstatt'
]

categories_for_restaurants = [
    'modern_european', 'scandinavian', 'caribbean', 'foodtours', 
    'gastropubs', 'italian', 'brasseries', 'ethiopian', 'spanish', 
    'popuprestaurants', 'greek', 'french', 'peruvian', 'british', 
    'mexican', 'restaurants', 'german', 'cuban', 'burmese', 
    'speakeasies', 'steak', 'basque', 'african', 'indonesian', 
    'fishnchips', 'mediterranean', 'localflavor', 'diners', 'latin', 
    'seafood', 'tapas', 'irish', 'breweries', 'himalayan', 'filipino', 
    'personalchefs', 'wine_bars', 'polish', 'austrian', 'honduran', 
    'ukrainian', 'raw_food', 'lebanese', 'portuguese', 'cocktailbars', 
    'asianfusion', 'cafeteria', 'tex-mex', 'vietnamese', 'pizza', 
    'thai', 'tapasmallplates', 'cajun', 'dinnertheater', 'tradamerican', 
    'whiskeybars', 'vegetarian', 'lounges', 'themedcafes', 'argentine', 
    'bars', 'turkish', 'vegan', 'venues', 'eventservices', 'australian', 
    'hungarian', 'pubs', 'chinese', 'fondue', 'catering', 'pancakes', 
    'hotels', 'korean', 'soup', 'nightlife', 'smokehouse', 'persian', 
    'hotelstravel', 'breakfast_brunch', 'gourmet', 'food_court', 'sushi', 
    'afghani', 'hawaiian', 'irish_pubs', 'beerbar', 'burgers', 'gluten_free', 
    'buffets', 'mideastern', 'russian', 'creperies', 'panasian', 'sportsbars', 
    'foodtrucks', 'streetvendors', 'tours', 'japanese', 'importedfood', 
    'delis', 'conveyorsushi', 'dimsum', 'brazilian', 'foodstands', 'kosher', 
    'salad', 'hotdog', 'cafes', 'seafoodmarkets', 'georgian', 'meats', 
    'singaporean', 'indpak', 'ramen', 'chicken_wings', 'bangladeshi', 
    'halal', 'falafel', 'bbq', 'moroccan', 'sandwiches', 'waffles', 
    'fooddeliveryservices', 'kebab', 'beer_and_wine', 'food', 
    'chickenshop', 'hotdogs', 'divebars', 'desserts', 'cheese', 
    'malaysian', 'arts', 'pakistani', 'popupshops', 'poke', 'taiwanese', 
    'musicvenues', 'professional', 'festivals', 'eventplanning', 
    'icecream', 'arabian', 'chocolate', 'candy'
]

categories_for_lieferservice = ['fooddeliveryservices', 'pizza', 'food']

categories_for_zum_abholen = ['panasian', 'trainstations', 'metrostations', 'greek', 'currysausage', 'publictransport', 'italian', 'thai', 'austrian', 'indonesian', 'german', 'beergarden', 'hotels', 'foodstands', 'vietnamese', 'bistros', 'hotelstravel', 'divebars', 'lounges', 'transport', 'restaurants', 'oriental', 'eventservices', 'icecream', 'airports', 'wok', 'pizza', 'korean', 'kebab', 'publicservicesgovt', 'sushi', 'international', 'mediterranean', 'burgers', 'cocktailbars', 'bars', 'vegetarian', 'falafel', 'hotdogs', 'cakeshop', 'delicatessen', 'indpak', 'pubs', 'nightlife', 'turkish', 'soup', 'vegan', 'steak', 'cafes', 'japanese', 'professional', 'fooddeliveryservices', 'beerbar', 'wine_bars', 'venues', 'autorepair', 'danceclubs', 'buffets', 'lebanese', 'salad', 'laundryservices', 'gluten_free', 'food']

categories_for_accountants = ['accountants', 'taxservices', 'financialadvising', 'professional', 'businessconsulting', 'notaries', 'financialservices', 'marketing', 'itservices']

categories_for_plumbers = ['plumbing', 'homeservices', 'hvac']

categories_for_autowerkstatt = ['autorepair', 'auto', 'car_dealers', 'towing', 'autopartssupplies', 'bodyshops', 'usedcardealers', 'tires', 'autodamageassessment', 'smog_check_stations']

# for desc in descs:
#     if desc == 'Restaurants':
#         categories = categories_for_restaurants
#     elif desc == 'Lieferservice':
#         categories = categories_for_lieferservice
#     elif desc == 'Zum Abholen':
#         categories = categories_for_zum_abholen
#     elif desc == 'Accountants':
#         categories = categories_for_accountants
#     elif desc == 'Plumbers':
#         categories = categories_for_plumbers
#     elif desc == 'Autowerkstatt':
#         categories = categories_for_autowerkstatt
    
#     for category in categories:
#         for postal_code in indexes:
#             Search.objects.get_or_create(
#                 decs=desc, category=category, postal_code=postal_code
#             )
#             print(f'{desc} - {category} - {postal_code} - created')

for desc in descs:
    for postal_code in indexes:
        SearchWitoutCategory.objects.get_or_create(
            decs=desc, postal_code=postal_code
        )
        print(f'{desc} - {postal_code} - created')