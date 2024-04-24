
import requests
from bs4 import BeautifulSoup


class UserBeerGetter:
    def get_beers_from_username(self, username):
        base_url = f"https://untappd.com/user/{username}/beers?sort=highest_rated_you"
        untappd_headers = {
            "Accept": "application/json", "Content-Type": "application/json",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Origin': 'https://untappd.com'
        }
        self.beers_info_dict = {}
        self.id = 0
        fist_25_beers_response = requests.get(url=base_url, headers=untappd_headers)
        if fist_25_beers_response.status_code == 200:
            self.beers_info_dict = self.get_beers_info(fist_25_beers_response)
        return self.beers_info_dict

    def get_beers_info(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        beers_div = soup.find('div', class_='distinct-list-list-container')
        beer_divs = beers_div.find_all('div', class_='beer-item')
        for beer_div in beer_divs:
            self.id += 1
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
            self.beers_info_dict[self.id] = beer_info_dict
        return self.beers_info_dict


# UserBeerGetter().get_beers_from_username('milovanp')
