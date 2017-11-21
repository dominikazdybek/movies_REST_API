from django.contrib import admin
from .models import Movie, Person, Cast

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "director", "year", "actors_list")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    list_display = ("role", "movie", "person")
