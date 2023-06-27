from django.urls import path

from . import views
from . import api

urlpatterns = [
    path("", views.index, name="index"),
    path("api/send/", api.send_message, name="api.send_message"),
    path("<str:room_name>/", views.room, name="room"),
]