import requests

from substitute.variable import NUTRITION_SCORE, CATEGORIES_OPEN_FOOD_FACTS, GROCERY_SHOP


class OpenFoodFactsAPIHandler:
    """ Handle the OpenFoodFacts API.
    """

    def __init__(self):
        """ Initialize some variables or objects.
        """
        # Empty the data storage
        self.api_answer = []
        self.substitutes_list = []
        self.filter_status = None

    def generate_substitutes_dict(self):
        """
        Generate an dictionary of substitutes from OFF API.
        """

        for single_cat in CATEGORIES_OPEN_FOOD_FACTS:
            # Send a request to the API
            self.fetch_data_from_cat(single_cat)

            # Ensure that all columns are filled
            self.check_data_integrity(single_cat)

    def fetch_data_from_cat(self, category):
        """
        Fetch aliments from specific :categories
        from the API through an HTTP instruction.
        Specify the nutrition_score wished and the store.
        """
        # Empty list
        self.api_answer.clear()

        # Fetching data from API to list
        for grade in NUTRITION_SCORE:
            for store in GROCERY_SHOP:
                # Generation of the request
                url = "https://fr.openfoodfacts.org/cgi/search.pl"
                criteria = {
                    "action": "process",

                    "tagtype_0": "categories",
                    "tag_contains_0": "contains",
                    "tag_0": category,

                    "tagtype_1": "countries",
                    "tag_contains_1": "contains",
                    "tag_1": "france",

                    "tagtype_2": "nutrition_grade_fr",
                    "tag_contains_2": "contains",
                    "tag_2": grade,

                    "tagtype_3": "product_name",
                    "tag_contains_3": "does_not_contain",
                    "tag_3": " ",

                    "tagtype_4": "stores",
                    "tag_contains_4": "contains",
                    "tag_4": store,

                    "sort_by": "product_name",
                    "page_size": 1,
                    "json": 1
                    }
                # Send a request to the API
                req = requests.get(url, params=criteria)
                # Fetching data in json file
                data = req.json()

                # Add data in the larger json file
                self.api_answer.extend(data['products'])

    def check_data_integrity(self, category_name):
        """Load the data if the whole details are
        available.
        """
        # Empty a dictionary
        columns_needed = {}

        # Format data
        for prod in self.api_answer:
            # Make sure that all fields are available
            if prod["product_name"]:
                try:
                    columns_needed["code"] = (prod["code"])
                    columns_needed["product_name"] = prod["product_name"]
                    columns_needed["categories"] = category_name
                    columns_needed["energy_value"] = prod["nutriments"]["energy_value"]
                    columns_needed["fat_value"] = prod["nutriments"]["fat_value"]
                    columns_needed["saturated-fat_value"] = prod["nutriments"]["saturated-fat_value"]
                    columns_needed["sugars_value"] = prod["nutriments"]["sugars_value"]
                    columns_needed["salt_value"] = prod["nutriments"]["salt_value"]
                    columns_needed["nutrition_grade_fr"] = prod["nutrition_grade_fr"]
                    columns_needed["store"] = prod["stores"]
                    columns_needed["Open_food_facts_url"] = prod["url"]
                    columns_needed["image_thumb_url"] = prod["image_thumb_url"]

                    # Add dictionary in the list
                    self.substitutes_list.append(dict(columns_needed))

                # Pass if some details are not available
                except KeyError:
                    pass
