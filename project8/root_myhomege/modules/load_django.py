import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'myhomege_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'myhomege_project.settings'

django.setup()
