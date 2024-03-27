import numpy as np

class UserPreferenceDeducer:
    def get_preference(self, beers):
        abv_ibu_prefs = self.deduce_abv_ibu(beers)

    def deduce_abv_ibu(self, beers_data):
        abv_values, ibu_values = self.extract_abv_and_ibu(beers_data)
        abv_min = np.min(abv_values)
        abv_max = np.max(abv_values)
        abv_mean = np.mean(abv_values)
        abv_quantiles = np.percentile(abv_values, [25, 50, 75])

        ibu_min = np.min(ibu_values)
        ibu_max = np.max(ibu_values)
        ibu_mean = np.mean(ibu_values)
        ibu_quantiles = np.percentile(ibu_values, [25, 50, 75])

        print("ABV Statistics:")
        print(f"Minimum ABV: {abv_min}")
        print(f"Maximum ABV: {abv_max}")
        print(f"Mean ABV: {abv_mean}")
        print("ABV Quantiles:")
        print(f"25th percentile: {abv_quantiles[0]}")
        print(f"Median (50th percentile): {abv_quantiles[1]}")
        print(f"75th percentile: {abv_quantiles[2]}")
        print()
        print("IBU Statistics:")
        print(f"Minimum IBU: {ibu_min}")
        print(f"Maximum IBU: {ibu_max}")
        print(f"Mean IBU: {ibu_mean}")
        print("IBU Quantiles:")
        print(f"25th percentile: {ibu_quantiles[0]}")
        print(f"Median (50th percentile): {ibu_quantiles[1]}")
        print(f"75th percentile: {ibu_quantiles[2]}")


        # return {
        #     'min_abv': min_abv,
        #     'max_abv': max_abv,
        #     'min_ibu': min_ibu,
        #     'max_ibu': max_ibu
        # }

    def extract_abv_and_ibu(self, beers_data):
        abv_values = []
        ibu_values = []
        for beer in beers_data.values():
            abv = float(beer['abv_text'].strip('% ABV '))
            abv_values.append(abv)
            if 'N/A' not in beer['ibu_text']:
                ibu = int(beer['ibu_text'].strip(' IBU '))
                ibu_values.append(ibu)

        return abv_values, ibu_values
