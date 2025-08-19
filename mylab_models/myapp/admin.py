from django.contrib import admin
from .models import Person, Musician, Album, Student

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    ordering = ['last_name', 'first_name']

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'instrument']
    list_filter = ['instrument']
    search_fields = ['first_name', 'last_name', 'instrument']

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'release_date', 'num_stars']
    list_filter = ['release_date', 'num_stars', 'artist']
    search_fields = ['name', 'artist__first_name', 'artist__last_name']
    date_hierarchy = 'release_date'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'year_in_school', 'get_year_display']
    list_filter = ['year_in_school']
    search_fields = ['name']
    
    def get_year_display(self, obj):
        return obj.get_year_in_school_display()
    get_year_display.short_description = 'Year Level'