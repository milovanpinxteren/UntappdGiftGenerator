import requests
from bs4 import BeautifulSoup

from giftGenerator.classes.user_preference_deducer import UserPreferenceDeducer


class UserBeerGetter:

    def get_beers_from_username(self, username):
        # username = 'milovanp'
        url = f"https://untappd.com/user/{username}/beers?sort=highest_rated_you"
        untappd_headers = {
            "Accept": "application/json", "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        # next url is https://untappd.com/profile/more_beer/{username}/25?sort=highest_rated_you
        # after https://untappd.com/profile/more_beer/{username}/50?sort=highest_rated_you
        # after https://untappd.com/profile/more_beer/{username}/75?sort=highest_rated_you
        # etc
        
        response = requests.get(url=url, headers=untappd_headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            beers_div = soup.find('div', class_='distinct-list-list-container')
            beer_divs = beers_div.find_all('div', class_='beer-item')
            beers_info_dict = {}
            id = 0
            for beer_div in beer_divs:
                id += 1
                name_tag = beer_div.find('p', class_='name')
                name = name_tag.find('a').text
                brewery_tag = beer_div.find('p', class_='brewery')
                brewery = brewery_tag.find('a').text
                ratings_div = soup.find('div', class_='ratings')
                ratings_divs = ratings_div.find_all('div', class_='you')
                abv_text = beer_div.find('p', class_='abv').text.strip()
                ibu_text = beer_div.find('p', class_='ibu').text.strip()
                beer_info_dict = {'name': name, 'brewery': brewery, 'abv_text': abv_text, 'ibu_text': ibu_text}
                for rating_div in ratings_divs:
                    caps_divs = rating_div.find_all('div', class_='caps')
                    data_rating_value = caps_divs[0]['data-rating']
                    if 'Global' in str(rating_div):
                        beer_info_dict['global_rating'] = float(data_rating_value)
                    elif 'Global' not in str(rating_div):
                        beer_info_dict['personal_rating'] = float(data_rating_value)
                beers_info_dict[id] = beer_info_dict
            return beers_info_dict

UserBeerGetter().get_beers_from_username()
