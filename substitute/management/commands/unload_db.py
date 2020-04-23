from django.core.management import BaseCommand
from substitute.data_base_handler import DataBaseTableHandler
from substitute.models import Aliment, UserLinkToAlimentsTable


class Command(BaseCommand):
    help = 'Load the DB from API'

    def handle(self, *args, **kwargs):
        # Remove data from table
        aliment_table_handler = DataBaseTableHandler(Aliment)
        aliment_table_handler.clear_table()
        favorite_table_handler = DataBaseTableHandler(UserLinkToAlimentsTable)
        favorite_table_handler.clear_table()
