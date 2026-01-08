import requests
from bs4 import BeautifulSoup
from django.utils.text import slugify
from gaming_app.models import Game

FEED_URL = "https://html5.gamemonetize.co/ip9pseepln2g3gv02ys3mkmzs3gegy8o/"


def sync_games():
    response = requests.get(FEED_URL, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "xml")

    games = soup.find_all("game")
    print(f"Found {len(games)} games")

    if not games:
        print("⚠️ No games found. Check feed URL or response content.")
        return

    for game in games:
        title_tag = game.find("title")
        if not title_tag:
            continue

        name = title_tag.text.strip()

        Game.objects.update_or_create(
            slug=slugify(name),
            defaults={
                "name": name,
                "description": game.findtext("description", ""),
                "category": game.findtext("category", "Other"),
                "thumbnail": game.findtext("thumb", ""),
                "url": game.findtext("url", ""),
            }
        )