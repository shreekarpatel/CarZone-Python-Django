from django.contrib import admin
from .models import Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    #we use this function to display img dynamically on admin site
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.photo.url))
    #giving title to thumbnail field as "Photo" 
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail','first_name', 'designation', 'created_date')
    list_display_links = ('id','thumbnail','first_name',)

    #by what field name you want to search("giving keyword from which it will search")
    search_fields = ('first_name', 'last_name', 'designation')

    #putting comma without having any field beside it because it is tuple and tuple tuple have more than one value in it.
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)