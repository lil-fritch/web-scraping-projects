import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'platformrealestateconz_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'platformrealestateconz.settings'

django.setup()
