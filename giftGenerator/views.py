from django.shortcuts import render

from giftGenerator.classes.menu_getter import MenuGetter
from giftGenerator.classes.user_beer_getter import UserBeerGetter
from giftGenerator.classes.user_preference_deducer import UserPreferenceDeducer
from giftGenerator.models import Venues


def index(request):
    print('hoi')
    return render(request, 'index.html')

def update_venue_menu(request):
    menu_getter = MenuGetter()
    if request.method == 'POST':
        venue_name = request.POST['venue_name']
        venue = Venues.objects.get(name=venue_name)
        if venue:
            menu_getter.get_untappd_menu(venue)
    return render(request, 'index.html')


def get_recommended_beers(request):
    user_beer_getter = UserBeerGetter()
    user_preference_deducer = UserPreferenceDeducer()
    if request.method == 'POST':
        untappd_username = request.POST['untappd_username']
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']
        beers = user_beer_getter.get_beers_from_username(untappd_username)
        user_preference = user_preference_deducer.deduce_abv_ibu(beers)

    return render(request, 'index.html')