import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'estitorcom_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'estitorcom_project.settings'

django.setup()
