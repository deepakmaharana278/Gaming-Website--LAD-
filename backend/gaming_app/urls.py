from django.urls import path
from .views import gamemonetize_games

urlpatterns = [
    path("games/", gamemonetize_games),
]
