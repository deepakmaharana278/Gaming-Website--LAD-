from django.core.management.base import BaseCommand
from gaming_app.services.gamemonitize import sync_games

class Command(BaseCommand):
    help = "Sync GameMonetize games"

    def handle(self, *args, **kwargs):
        sync_games()
        self.stdout.write(self.style.SUCCESS("Games synced successfully"))
