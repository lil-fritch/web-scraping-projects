import sys
import os
import django

sys.path.append('C:\\Users\\fritch\\Downloads\\Telegram Desktop\\chats_export\\chats_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'chats_project.settings'
django.setup()