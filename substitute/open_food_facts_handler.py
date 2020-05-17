import requests

from substitute import variable
from substitute.variable import NUTRITION_SCORE, FOOD_CATEGORIES, GROCERY_BRAND


class OpenFoodFactsAPIHandler:
    """ Handle the OpenFoodFacts (OFF) API.
    """

    def __init__(self):
        """ Initialize some variables or objects.
        """
        # Empty the data storage
        self.api_answer = []
        self.substitutes_list = []
        self.code_list = []
        self.filter_status = None
        self.criteria = Criteria()

    def generate_substitutes_dict(self):
        """
        Generate an dictionary of substitutes from OFF API.
        """

        # Initialise
        self.api_answer.clear()
        self.code_list.clear()

        for store in self.criteria.get_grocery_brand():
            for category in self.criteria.get_categories():
                for grade in self.criteria.get_nutriscore():
                    # Send a request to the API
                    self.api_answer.extend(self.fetch_data_from_api(category, grade, store))

            # Ensure that all columns are filled
            self.check_data_integrity(category, grade, store)

    def fetch_data_from_api(self, category_wished, grade_wished, store_wished):
        """
        Fetch aliments from specific :category, :grade, :store
        from the API through an HTTP instruction.
        """

        # Generation of the request
        url = "https://fr.openfoodfacts.org/cgi/search.pl"
        criteria = {
            "action": "process",

            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category_wished,

            "tagtype_1": "countries",
            "tag_contains_1": "contains",
            "tag_1": "france",

            "tagtype_2": "nutrition_grade_fr",
            "tag_contains_2": "contains",
            "tag_2": grade_wished,

            "tagtype_3": "product_name",
            "tag_contains_3": "does_not_contain",
            "tag_3": " ",

            "tagtype_4": "stores",
            "tag_contains_4": "contains",
            "tag_4": store_wished,

            "sort_by": "product_name",
            "page_size": 1,
            "json": 1
            }
        # Send a request to the API
        req = requests.get(url, params=criteria)
        # Fetching data in json file
        data = req.json()

        # Add data in the larger json file
        #self.api_answer.extend(data['products'])

        return data['products']

    def check_data_integrity(self, category_name, grade_name, store_name):
        """Load the data if the whole details are
        available.
        """
        # Empty a dictionary
        columns_needed = {}

        # Format data
        for prod in self.api_answer:
            # Make sure that all fields are available
            if prod["product_name"]:
                if prod["code"] not in self.code_list:
                    try:
                        columns_needed["code"] = prod["code"]
                        columns_needed["product_name"] = prod["product_name"]
                        columns_needed["categories"] = category_name
                        columns_needed["energy_value"] = prod["nutriments"]["energy_value"]
                        columns_needed["fat_value"] = prod["nutriments"]["fat_value"]
                        columns_needed["saturated-fat_value"] = prod["nutriments"]["saturated-fat_value"]
                        columns_needed["sugars_value"] = prod["nutriments"]["sugars_value"]
                        columns_needed["salt_value"] = prod["nutriments"]["salt_value"]
                        columns_needed["nutrition_grade_fr"] = grade_name
                        columns_needed["store"] = store_name
                        columns_needed["Open_food_facts_url"] = prod["url"]
                        columns_needed["image_thumb_url"] = prod["image_thumb_url"]

                        # Add dictionary in the list
                        self.substitutes_list.append(dict(columns_needed))

                        # Add in the "already recorded" code list
                        self.code_list.append(prod["code"])

                    # Pass if some details are not available
                    except KeyError:
                        pass
                else:
                    print(prod["product_name"] + "is already in the list.")


class Criteria:

    def get_categories(self):
        return variable.FOOD_CATEGORIES

    def get_nutriscore(self):
        return variable.NUTRITION_SCORE

    def get_grocery_brand(self):
        return variable.GROCERY_BRAND
