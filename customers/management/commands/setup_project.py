import os

from django.core.management import BaseCommand


class Command(BaseCommand):
    help='Setup project dependencies'
    
    def handle(self, *args, **kwargs):
        os.system('pip install django-extensions')
        os.system('pip install python-dotenv')
        os.system('pip install djangorestframework')
        os.system('python manage.py migrate')
        os.system('python manage.py load_customers')
        
