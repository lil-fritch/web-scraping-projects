import os
import sys
import django

# Додаємо шлях до проекту
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'yad2coil_project')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'yad2coil_project.settings'

django.setup()
