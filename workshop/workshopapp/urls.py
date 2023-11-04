from django.urls import path

from . import views

app_name = "workshopapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("frames/", views.frames, name="frames"),
    path("frames/<int:frame_id>/", views.frame, name="frame"),
    path("contacts/", views.contacts, name="contacts"),
    path("about/", views.about, name="about"),
]
