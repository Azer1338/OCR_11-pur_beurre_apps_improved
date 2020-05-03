from unittest.mock import MagicMock

from django.test import TestCase
from django.urls import reverse
from accounts.models import PurBeurreUser
from .data_base_handler import DataBaseTableHandler
from .models import Aliment, UserLinkToAlimentsTable
from .open_food_facts_handler import OpenFoodFactsAPIHandler


# search_view page
class SearchPageTestCase(TestCase):

    def setUp(self):
        """ Set up variables before launching tests.
        """
        # Creation of an aliment
        aliment_1 = Aliment.objects.create(
            id="01",
            code="1",
            name="Patate",
            category="legumes",
            energy="1",
            fat="1",
            fat_saturated="1",
            sugar="1",
            salt="1",
            nutrition_score="a",
            url_link="http://google.com/1",
            picture_link="http://google.com/1",
        )
        aliment_1.save()

        # Creation of an other aliment
        aliment_2 = Aliment.objects.create(
            id="02",
            code="2",
            name="Oignons",
            category="legumes",
            energy="2",
            fat="2",
            fat_saturated="2",
            sugar="2",
            salt="2",
            nutrition_score="b",
            url_link="http://google.com/2",
            picture_link="http://google.com/2",
        )
        aliment_2.save()

    def test_search_page_return_message_on_emptied_query(self):
        response = self.client.get(reverse('substitute:search'), {'userSearch': ''})
        # Check the return message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['message']),
                         "Vous n'avez pas spécifié votre recherche. Voici notre liste."
                         )

    def test_search_page_return_message_on_known_query(self):
        response = self.client.get(reverse('substitute:search'), {'userSearch': 'patate'})
        # Check the return message
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(str(response.context['message']),
                            "Vous n'avez pas spécifié votre recherche. Voici notre liste."
                            )

    def test_search_page_return_list_against_known_product(self):
        response = self.client.get(reverse('substitute:search'), {'userSearch': 'patate'})
        # Check the existence of the second aliment in the list
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['substitutes'].object_list[1].name,
                         "Oignons"
                         )
        self.assertNotEqual(response.context['substitutes'].object_list[1].name,
                            "Patate"
                            )

    def test_search_page_return_list_against_unknown_product(self):
        response = self.client.get(reverse('substitute:search'), {'userSearch': 'chocolat'})
        # Check the return message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['message']),
                         "Misère de misère, nous n'avons trouvé aucun résultat !"
                         )


# detail_view Page
class DetailPageTestCase(TestCase):

    def setUp(self):
        """ Set up variables before launching tests.
        """
        # Creation of an aliment
        aliment_1 = Aliment.objects.create(
            id="01",
            code="1",
            name="Patate",
            category="legumes",
            energy="1",
            fat="1",
            fat_saturated="1",
            sugar="1",
            salt="1",
            nutrition_score="a",
            url_link="http://google.com/1",
            picture_link="http://google.com/1",
        )
        aliment_1.save()

    def test_detail_page_with_a_known_item(self):
        response = self.client.get('/substitute/details/1/')
        # Check the existence of the category in the page
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['aliment'].category), 'legumes')


# favorites_view page
class FavoritePageTestCase(TestCase):

    def setUp(self):
        """ Set up variables before launching tests.
        """
        # Creation of an aliment
        aliment_1 = Aliment.objects.create(
            id="01",
            code="1",
            name="Patate",
            category="legumes",
            energy="1",
            fat="1",
            fat_saturated="1",
            sugar="1",
            salt="1",
            nutrition_score="a",
            url_link="http://google.com/1",
            picture_link="http://google.com/1",
        )
        aliment_1.save()

        # Creation of a second aliment
        aliment_2 = Aliment.objects.create(
            id="02",
            code="2",
            name="Oignons",
            category="legumes",
            energy="2",
            fat="2",
            fat_saturated="2",
            sugar="2",
            salt="2",
            nutrition_score="b",
            url_link="http://google.com/2",
            picture_link="http://google.com/2",
        )
        aliment_2.save()

        # Creation of an user
        test_user_1 = PurBeurreUser.objects.create_user(email="Franco13@.com",
                                                        first_name="claude",
                                                        name="francois",
                                                        password="Chanson",
                                                        city='Brignoles'
                                                        )
        test_user_1.save()
        # User is authenticated
        self.client.login(username="Franco13@.com", password="Chanson")

    def test_favorite_page_return_message_on_existing_favorites(self):
        # Create a link between aliments and the user
        link_1 = UserLinkToAlimentsTable.objects.create(
            user_id="Franco13@.com",
            aliment_id=0
        )
        link_1.save()
        # Create a second link between aliments and the user
        link_2 = UserLinkToAlimentsTable.objects.create(
            user_id="Franco13@.com",
            aliment_id=1
        )
        link_2.save()

        response = self.client.get(reverse('substitute:favorites'))
        # Check the message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['message']),
                         "Voici vos favoris"
                         )

    def test_favorite_page_return_message_on_not_existing_favorites(self):
        response = self.client.get(reverse('substitute:favorites'))
        # Check the message
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['message']),
                         "Misère de misère, vous n'avez encore pas enregistrer de favoris !"
                         )


# save_view page
class SavePageTestCase(TestCase):

    def setUp(self):
        """ Set up variables before launching tests.
        """
        # Creation of an aliment
        aliment_1 = Aliment.objects.create(
            id="01",
            code="1",
            name="Patate",
            category="legumes",
            energy="1",
            fat="1",
            fat_saturated="1",
            sugar="1",
            salt="1",
            nutrition_score="a",
            url_link="http://google.com/1",
            picture_link="http://google.com/1",
        )
        aliment_1.save()

        # Creation of an user
        test_user_1 = PurBeurreUser.objects.create_user(email="Franco13@.com",
                                                        first_name="claude",
                                                        name="francois",
                                                        password="Chanson",
                                                        city='Toulouse'
                                                        )
        test_user_1.save()
        # User is authenticated
        self.client.login(username="Franco13@.com", password="Chanson")

    def test_save_page_return_302(self):
        response = self.client.get('/substitute/save/1/', HTTP_REFERER='/substitute/favorites/')
        # Check the redirection
        self.assertRedirects(response, '/substitute/favorites/', status_code=302)


# delete_view page
class DeletePageTestCase(TestCase):

    def setUp(self):
        """ Set up variables before launching tests.
        """
        # Creation of an aliment
        aliment_1 = Aliment.objects.create(
            id="01",
            code="1",
            name="Patate",
            category="legumes",
            energy="1",
            fat="1",
            fat_saturated="1",
            sugar="1",
            salt="1",
            nutrition_score="a",
            url_link="http://google.com/1",
            picture_link="http://google.com/1",
        )
        aliment_1.save()

        # Creation of an user
        test_user_1 = PurBeurreUser.objects.create_user(email="Franco13@.com",
                                                        first_name="claude",
                                                        name="francois",
                                                        password="Chanson",
                                                        city="Grenoble"
                                                        )
        test_user_1.save()
        # User is authenticated
        self.client.login(username="Franco13@.com", password="Chanson")

    def test_delete_page_return_302(self):
        response = self.client.get('/substitute/delete/1/', HTTP_REFERER='/substitute/favorites/')
        # Check the redirection
        self.assertRedirects(response, '/substitute/favorites/', status_code=302)


# Aliment model
class AlimentTest(TestCase):

    def create_aliment(self,
                       id="01",
                       code="1",
                       name="Patate",
                       category="legumes",
                       energy="1",
                       fat="1",
                       fat_saturated="1",
                       sugar="1",
                       salt="1",
                       nutrition_score="a",
                       url_link="http://google.com/1",
                       picture_link="http://google.com/1",
                       ):
        return Aliment.objects.create(id=id,
                                      code=code,
                                      name=name,
                                      category=category,
                                      energy=energy,
                                      fat=fat,
                                      fat_saturated=fat_saturated,
                                      sugar=sugar,
                                      salt=salt,
                                      nutrition_score=nutrition_score,
                                      url_link=url_link,
                                      picture_link=picture_link,
                                      )

    def test_myUser_creation(self):
        a = self.create_aliment()
        self.assertTrue(isinstance(a, Aliment))


# UserLinkToAlimentsTable model
class UserLinkToAlimentsTableTest(TestCase):

    def create_userLinkToAlimentsTable(self,
                                       user_id="01",
                                       aliment_id="10",
                                       ):
        return UserLinkToAlimentsTable.objects.create(user_id=user_id,
                                                      aliment_id=aliment_id,
                                                      )

    def test_myUser_creation(self):
        u = self.create_userLinkToAlimentsTable()
        self.assertTrue(isinstance(u, UserLinkToAlimentsTable))


# OpenFoodFactsAPIHandler
class OpenFoodFactsAPIHandlerTest(TestCase):

    def test_open_food_facts_handler_creation(self):
        handler = OpenFoodFactsAPIHandler()

        self.assertEqual(handler.api_answer, [])
        self.assertEqual(handler.substitutes_list, [])
        self.assertEqual(handler.filter_status, None)

    def test_open_food_facts_handler_api_mock(self):
        handler = OpenFoodFactsAPIHandler()
        # Mock the API call
        handler.fetch_data_from_cat = MagicMock(return_value=0)
        handler.api_answer = [{'code': '01',
                               'product_name': 'test name',
                               'category_name': 'test cat',
                               'nutriments': {'energy_value': '03',
                                              'fat_value': '03',
                                              'saturated-fat_value': '03',
                                              'sugars_value': '03',
                                              'salt_value': '03'},
                               'nutrition_grade_fr': 'test nut',
                               'stores': 'Carrefour',
                               'url': 'google.com',
                               'image_thumb_url': 'google.com/test',
                               }
                              ]

        # Keep going on process
        handler.generate_substitutes_dict()

        self.assertEqual(handler.substitutes_list, [{'code': '01',
                                                     'product_name': 'test name',
                                                     'categories': 'Sirop',
                                                     'energy_value': '03',
                                                     'fat_value': '03',
                                                     'saturated-fat_value': '03',
                                                     'sugars_value': '03',
                                                     'salt_value': '03',
                                                     'nutrition_grade_fr': 'test nut',
                                                     'store': 'Carrefour',
                                                     'Open_food_facts_url': 'google.com',
                                                     'image_thumb_url': 'google.com/test',
                                                     },
                                                    {'code': '01',
                                                     'product_name': 'test name',
                                                     'categories': 'Tarte',
                                                     'energy_value': '03',
                                                     'fat_value': '03',
                                                     'saturated-fat_value': '03',
                                                     'sugars_value': '03',
                                                     'salt_value': '03',
                                                     'nutrition_grade_fr': 'test nut',
                                                     'store': 'Carrefour',
                                                     'Open_food_facts_url': 'google.com',
                                                     'image_thumb_url': 'google.com/test',
                                                     },
                                                    ])


# DataBaseTableHandler
class DataBaseTableHandlerTest(TestCase):

    def test_database_handler_creation(self):
        table_test = Aliment
        handler = DataBaseTableHandler(table_test)

        self.assertEqual(handler.table_impacted, table_test)
        self.assertEqual(handler.list_loaded_length, 0)
        self.assertEqual(handler.message, 'Initiate')

    def test_load_data_in_aliment_table(self):
        table_test = Aliment
        handler = DataBaseTableHandler(table_test)
        table_to_load = [{'code': '01',
                          'product_name': 'test name',
                          'categories': 'Soda',
                          'energy_value': '03',
                          'fat_value': '03',
                          'saturated-fat_value': '03',
                          'sugars_value': '03',
                          'salt_value': '03',
                          'nutrition_grade_fr': 'test nut',
                          'Open_food_facts_url': 'google.com',
                          'image_thumb_url': 'google.com/test',
                          'store': 'Carrefour',
                          }]

        # Load in table
        handler.load_json_file_in_table(table_to_load)

        # Collect from Database
        list_from_table = table_test.objects.all()

        for elt in list_from_table:
            name = elt.name

        self.assertEqual(handler.message, "Table loaded")
        self.assertEqual(name, 'test name')



