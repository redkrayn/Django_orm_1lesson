import os

from django.core.management import execute_from_command_line

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'  # Затычка, без этого не работает
execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())
