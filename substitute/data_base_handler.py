

class DataBaseTableHandler:
    """
    Handle a table in the database.
    """

    def __init__(self, table):
        """
        Initialisation.
        :param table: table targeted for modifications
        """
        self.table_impacted = table
        self.list_loaded_length = 0
        self.message = "Initiate"

    def load_json_file_in_table(self, json_file):
        """
        Load data in the table.
        :param json_file: data json file to load.
        """
        # Status change
        self.message = "Table is loading."
        print(self.message)

        # Fill details and load it
        for elt in json_file:
            self.table_impacted.objects.create(code=elt['code'],
                                               name=elt['product_name'],
                                               category=elt['categories'],
                                               energy=elt['energy_value'],
                                               fat=elt['fat_value'],
                                               fat_saturated=elt['saturated-fat_value'],
                                               sugar=elt['sugars_value'],
                                               salt=elt['salt_value'],
                                               nutrition_score=elt['nutrition_grade_fr'],
                                               url_link=elt['Open_food_facts_url'],
                                               picture_link=elt['image_thumb_url'],
                                               )

        # Number of elements loaded
        self.list_loaded_length = len(json_file)
        print("Database size: " + str(self.list_loaded_length))

        # Status change
        self.message = "Table loaded"
        print(str(self.table_impacted) + " " + self.message)

    def clear_table(self):
        """
        Remove data from the table
        """
        # Select all element and remove it
        self.table_impacted.objects.all().delete()

        # Status change
        self.message = "Table emptied"
        print(str(self.table_impacted) + " " + self.message)
