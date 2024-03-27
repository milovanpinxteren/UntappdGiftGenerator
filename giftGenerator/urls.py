from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', views.index, name='index'),
    path("update_venue_menu", views.update_venue_menu, name="update_venue_menu"),
    path("get_recommended_beers", views.get_recommended_beers, name="get_recommended_beers"),
    ]