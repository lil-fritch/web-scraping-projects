import os
import sys
import django

# Додаємо шлях до проекту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'myhomeie_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'myhomeie_project.settings'

django.setup()
