import requests
from bs4 import BeautifulSoup

from load_django import *
from parser_app.models import *

from selenium_launcher import SeleniumDriver

from emails_by_popular import EmailExtractor
from emails_mailto import MailtoEmailExtractor
from social import SocialLinksExtractor

from email_domains import top_email_domains

driver = SeleniumDriver()

email_extractor = EmailExtractor(top_email_domains)
social_extractor = SocialLinksExtractor(driver.get_driver())

for item in Place.objects.filter(status='New'):
    if not item.website:
        item.status = 'Done'
        item.save()
        continue
    
    try:
        response = requests.get(item.website)
    except:
        print('Error: Could not load the page')
        item.status = 'LoadError'
        item.save()
        continue    
    
    emails = email_extractor.extract(response.text)
    if not emails:
        extractor = MailtoEmailExtractor(response.text)
        emails = extractor.find_emails()
    if not emails:
        emails = None
    item.email = emails    
    
    driver.load_url(item.website)
    extracted_links = social_extractor.extract_links()
    
    item.instagram = extracted_links.get('instagram')
    item.facebook = extracted_links.get('facebook')
    item.twitter = extracted_links.get('twitter')
    item.linkedin = extracted_links.get('linkedin')

    item.status = 'Done'
    item.save()
    
    print(emails, extracted_links)    