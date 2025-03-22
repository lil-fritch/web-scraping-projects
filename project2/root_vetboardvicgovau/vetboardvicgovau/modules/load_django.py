import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'vetboardvicgovau_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'vetboardvicgovau.settings'

django.setup()
