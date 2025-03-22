import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lamudicomph_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'lamudicomph.settings'

django.setup()
