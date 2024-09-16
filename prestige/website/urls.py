from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"), 
    path("services/", views.services, name="services"),
    path("specialties/", views.specialties, name="specialties"),
    path("teams/", views.teams, name="teams"),
    path("appointment/", views.appointment, name="appointment"),
    path("contact/", views.contact, name="contact"),
]