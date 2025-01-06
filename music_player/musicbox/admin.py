from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from musicbox.models import User

from musicbox.models import Artist,Album,Genre

from musicbox.models import Playlist,LikedSong,SongTrack

# Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(LikedSong)
admin.site.register(SongTrack)