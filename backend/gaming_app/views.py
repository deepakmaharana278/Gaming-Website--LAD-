from django.http import JsonResponse
import requests
import feedparser
import time

CACHE = {
    "data": None,
    "time": 0
}

FEED_URL = "https://gamemonetize.com/feed.php?format=1&num=200&page=1"

def gamemonetize_games(request):
    now = time.time()

    # 30 min cache
    if CACHE["data"] and now - CACHE["time"] < 1800:
        return JsonResponse(CACHE["data"], safe=False)

    feed = feedparser.parse(FEED_URL)

    games = []

    for entry in feed.entries:
        games.append({
            "id": entry.id if "id" in entry else "",
            "title": entry.title,
            "description": entry.description,
            "instructions": entry.get("instructions", ""),
            "category": entry.get("category", ""),
            "tags": [t.term for t in entry.tags] if "tags" in entry else [],
            "url": entry.get("url", ""),
            "thumb": entry.get("thumb", ""),
        })

    CACHE["data"] = games
    CACHE["time"] = now

    return JsonResponse(games, safe=False)
