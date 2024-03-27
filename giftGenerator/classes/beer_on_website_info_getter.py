import requests
from bs4 import BeautifulSoup
import unicodedata
import re
# from giftGenerator.models import Venues


class BeerOnWebsiteInfoGetter:
    def get_info(self, venue, name):
        normalized_name = unicodedata.normalize('NFKD', name)
        cleaned_name = re.sub(r'[^\w\s]', '', normalized_name)
        url = venue.venue_website_url + '/search?q='+ cleaned_name.replace(' ', '+')
        print(url)
        headers = {
            "Accept": "application/json", "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find('ul', class_='product-grid')
        try:
            best_result = results.find_all('li')[0]
            price = best_result.find('div', class_='price__container').find('span', class_='price-item--regular').text
            cleaned_price = float(price.strip().replace('€', '').replace(',', '.'))
            a_tag = best_result.find('div', class_='card__information').find('a')
            if a_tag:
                beer_url = venue.venue_website_url + a_tag['href']
        except Exception as e: #if no search results
            cleaned_price = None
            beer_url = None
        return cleaned_price, beer_url

# PriceGetter().update_prices(venue = 'https://houseofbeers.nl/search?q=', name='Goose Island')