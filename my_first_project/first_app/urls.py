from django.urls import path
from first_app.views import *
urlpatterns = [
    path("", index,name='index'),
    path("musician-form/", musician_form,name='musician_form'),
    path("album-form/", album_form,name='album_form'),
    path("album-list/<int:artist_id>/", album_list,name='album_list'),
    path("edit-artist/<int:artist_id>/", edit_artist,name='edit_artist'),
    path("edit-album/<int:album_id>/", edit_album,name='edit_album'),
    path("delete-album/<int:album_id>/", delete_album,name='delete_album'),
    path("delete-artist/<int:artist_id>/", delete_musician,name='delete_musician'),
]
