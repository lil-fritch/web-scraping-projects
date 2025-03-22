import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'indomioalenagents_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'indomioalenagents_project.settings'

django.setup()
