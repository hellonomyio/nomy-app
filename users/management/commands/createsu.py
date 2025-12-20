from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = "Create a superuser without prompt"

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")

        if not username or not password:
            self.stdout.write("Missing credentials")
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write("Superuser already exists")
            return

        User.objects.create_superuser(username=username, password=password, email=email)
        self.stdout.write("Superuser created")
