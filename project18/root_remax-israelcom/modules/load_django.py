import os
import sys
import django

# Додаємо шлях до проекту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'remaxisraelcom_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'remaxisraelcom_project.settings'

django.setup()
