import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.utils.text import slugify
from gaming_app.models import Game

def sync_games():
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
    }

    response = requests.get(
        settings.GAMEMONETIZE_FEED_URL,
        headers=headers,
        timeout=30
    )
    response.raise_for_status()

    # 🔍 DEBUG (temporary – keep for now)
    print("STATUS:", response.status_code)
    print("CONTENT-TYPE:", response.headers.get("Content-Type"))
    print("FIRST 300 CHARS:\n", response.text[:300])

    # ✅ ALWAYS PARSE AS XML
    soup = BeautifulSoup(response.content, "xml")
    games = soup.find_all("game")

    if not games:
        print("❌ No <game> tags found. Feed is NOT valid XML.")
        return

    created, updated = 0, 0

    for g in games:
        name = g.findtext("title", "").strip()
        if not name:
            continue

        slug = slugify(name)[:240]

        _, is_created = Game.objects.update_or_create(
            slug=slug,
            defaults={
                "name": name,
                "description": g.findtext("description", ""),
                "category": g.findtext("category", "Other"),
                "thumbnail": g.findtext("thumb", ""),
                "url": g.findtext("url", ""),
                "source": "GameMonetize",
            }
        )

        if is_created:
            created += 1
        else:
            updated += 1

    print(f"Sync complete → Created: {created}, Updated: {updated}")
