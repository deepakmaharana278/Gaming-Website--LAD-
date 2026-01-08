from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    thumbnail = models.URLField()
    url = models.URLField()
    source = models.CharField(max_length=50, default="GameMonetize")

    def __str__(self):
        return self.name