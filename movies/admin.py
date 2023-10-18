from django.contrib import admin
from .models import Genre, Movie

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# With exclude with specify the fields to not show when creating
# a new movie record

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('id', 'title', 'number_in_stock', 'daily_rate')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
