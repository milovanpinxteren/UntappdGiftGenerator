import requests
from bs4 import BeautifulSoup

from giftGenerator.classes.beer_on_website_info_getter import BeerOnWebsiteInfoGetter
from giftGenerator.models import Venues, Beers


class MenuGetter:
    def get_untappd_menu(self, venue):
        self.price_getter = BeerOnWebsiteInfoGetter()
        untappd_headers = {
            "Accept": "application/json", "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        response = requests.get(url=venue.untappd_url, headers=untappd_headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            menu_ul = soup.find('ul', class_='menu-section-list')
            beer_divs = menu_ul.find_all('li', class_='menu-item')
            for beer_div in beer_divs:
                name = beer_div.find('a', {'data-href': ':'}).text.strip()
                url = "https://untappd.com" + beer_div.find('a', class_='track-click', attrs={'data-href': ':'}).get(
                    'href')
                brewery = beer_div.find('a', {'data-href': ':brewery'}).text.strip()
                rating_div = beer_div.find('div', {'class': 'caps small'})
                rating_value = rating_div['data-rating']
                abv_ibu_span = beer_div.find('span').text.strip()
                abv = None
                if 'ABV' in abv_ibu_span:
                    abv_raw_text = abv_ibu_span.split('ABV')[0].strip()
                    if 'N/A' not in abv_raw_text:
                        abv = abv_raw_text.replace('%', '')
                        if abv.replace('.', '', 1).isdigit():  # Check if it is a valid number
                            abv = float(abv)
                ibu = None
                if 'IBU' in abv_ibu_span:
                    ibu_raw_text = abv_ibu_span.split('IBU')[0].split('•')[-1].strip()
                    if 'N/A' not in ibu_raw_text:
                        if ibu_raw_text.replace('.', '', 1).isdigit():  # Check if it is a valid number
                            ibu = float(ibu_raw_text)

                price, beer_url = self.price_getter.get_info(venue, name)

                if not Beers.objects.filter(name=name).exists():
                    # If it doesn't exist, add it to the Beers model
                    Beers.objects.create(name=name, brewery=brewery, untappd_url=url, abv=abv, ibu=ibu,
                                         price=price, venue_website_url=beer_url, rating=rating_value, venue_id=venue.id)
