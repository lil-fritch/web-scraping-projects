import os
import sys
import django

# Додаємо шлях до проекту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'yelpde_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'yelpde_project.settings'

django.setup()
