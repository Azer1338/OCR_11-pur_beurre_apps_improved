from django.test import TestCase
from django.urls import reverse
from django_forms_test import FormTest, field

from accounts.forms import RegisterForm, MyUserAdminCreationForm
from accounts.models import PurBeurreUser


# my_account_view page
class AccountPageTestCase(TestCase):

    def setUp(self):
        """ Set up variables before launching tests.
        """
        # Creation of an user
        test_user = PurBeurreUser.objects.create_user(email="Franco13@.com",
                                                      first_name="claude",
                                                      name="francois",
                                                      password="Chanson"
                                                      )
        test_user.save()

    # test page returns 200
    def test_account_page_return_200_when_user_is_connected(self):
        # Authenticate an user
        self.client.login(username="Franco13@.com", password="Chanson")
        response = self.client.get(reverse('accounts:myAccount'))
        # Look for the user
        self.assertEqual(str(response.context['user']), "Franco13@.com")

        self.assertEqual(response.status_code, 200)

    # test page doesn't return 200
    def test_account_page_return_200_when_user_is_not_connected(self):
        response = self.client.get(reverse('accounts:myAccount'))

        self.assertNotEqual(response.status_code, 200)


# signup_view page
class SignupPageTestCase(TestCase):

    # test page returns a 200
    def test_signup_page_return_200_on_GET_method(self):
        response = self.client.get(reverse('accounts:signup'))

        self.assertEqual(response.status_code, 200)

    # test page returns a 200
    def test_signup_page_return_200_on_POST_method(self):
        # Request comes with authentication data
        response = self.client.post(reverse('accounts:signup'),
                                    data={'email': 'hubert.f@gmail.com',
                                          'first_name': 'hubert',
                                          'name': 'f'})

        self.assertEqual(response.status_code, 200)


# login_view page
class LoginPageTestCase(TestCase):

    # test page returns a 200
    def test_login_page_return_200_on_GET_method(self):
        response = self.client.get(reverse('accounts:login'))

        self.assertEqual(response.status_code, 200)

    # test page returns a 200
    def test_login_page_return_200_with_a_POST_method(self):
        # Request comes with authentication data
        response = self.client.post(reverse('accounts:signup'),
                                    data={'username': 'hubert.f@gmail.com',
                                          'password': 'hubert'})

        self.assertEqual(response.status_code, 200)


# logout_view page
class LogoutPageTestCase(TestCase):

    def setUp(self):
        """ Set up variables before launching tests.
        """
        # Creation of an user
        test_user = PurBeurreUser.objects.create_user(email="Franco13@.com",
                                                      first_name="claude",
                                                      name="francois",
                                                      password="Chanson"
                                                      )
        test_user.save()

        # Authenticate an user
        self.client.login(username="Franco13@.com", password="Chanson")

    # test that page returns a 200
    def test_logout_page_return_200_when_user_is_connected(self):
        # Disconnect the user
        response = self.client.get(reverse('accounts:logout'))
        # Check that an user is connected
        self.assertNotEqual(str(response.context['user']), "Franco13@.com")

        self.assertEqual(response.status_code, 200)

    # test that page returns a 200
    def test_logout_page_return_200_when_user_not_connected(self):
        response = self.client.get(reverse('accounts:logout'))

        self.assertEqual(response.status_code, 200)


# MyUser models
class MyUserTest(TestCase):

    # Models
    def test_create_myUser(self, email="bobo@genoise.mousse",
                           first_name="bob", name="o"):
        return PurBeurreUser.objects.create_user(email=email,
                                                 first_name=first_name,
                                                 name=name,
                                                 password=None
                                                 )

    def test_myUser_creation(self):
        u = self.create_myUser()
        self.assertTrue(isinstance(u, PurBeurreUser))


# RegisterForm form
class RegisterFormTest(FormTest):

    form = RegisterForm
    required_fields = [
        ('email', field.EMAIL),
        ('password', field.PASSWORD),
        ('password2', field.PASSWORD),
    ]


# MyUserAdminCreationForm form
class MyUserAdminCreationFormTest(FormTest):
    form = MyUserAdminCreationForm
    required_fields = [
        ('email', field.EMAIL),
        ('password1', field.PASSWORD),
        ('password2', field.PASSWORD),
    ]
