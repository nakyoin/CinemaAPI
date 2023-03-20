from django.db import models
from rest_framework import serializers

class Films(models.Model):
    title = models.CharField(max_length=100)
    date_out = models.DateTimeField(default=None)
    country = models.CharField(max_length=100)
    director_film = models.ForeignKey('Director', on_delete=models.PROTECT, related_name="dir")
    genre_film = models.ForeignKey('Genre', on_delete=models.PROTECT, related_name="gen")

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return str(self.title)

class Director(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

    def __str__(self):
        return str(self.name)

class Genre(models.Model):
    genres = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return str(self.genres)


class Afisha(models.Model):
    dates = models.DateTimeField(default=None)
    films_existed = models.ForeignKey('Films', blank=True, related_name='af', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Афиша'
        verbose_name_plural = 'Афиши'

    def __str__(self):
        return str(self.films_existed)