from django.core.management import BaseCommand
from substitute.data_base_handler import DataBaseTableHandler
from substitute.models import Aliment
from substitute.open_food_facts_handler import OpenFoodFactsAPIHandler


class Command(BaseCommand):
    help = 'Load the DB from API'

    def handle(self, *args, **kwargs):
        # Gather data from API
        api_handler = OpenFoodFactsAPIHandler()
        api_handler.generate_substitutes_dict()

        # Load data in the database
        aliment_table_handler = DataBaseTableHandler(Aliment)
        aliment_table_handler.load_json_file_in_table(api_handler.substitutes_list)
