from django.core.management.base import BaseCommand
from ...models import User
import os
from dotenv import load_dotenv
    
load_dotenv()

class Command(BaseCommand):

    def handle(self, *args, **options):
        email = os.getenv('ADMIN_EMAIL')
        password = os.getenv('ADMIN_PASSWORD')

        if email != None and password != None:
            if not User.objects.filter(email=email).exists():
                User.objects.create_superuser(email=email, password=password)