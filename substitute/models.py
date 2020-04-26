from django.db import models

# from accounts.models import MyUser


class Aliment(models.Model):
    code = models.CharField(max_length=500, unique=False)
    name = models.CharField(max_length=501, unique=False)
    category = models.CharField(max_length=502, unique=False)
    energy = models.FloatField(max_length=503, unique=False)
    fat = models.FloatField(max_length=504, unique=False)
    fat_saturated = models.FloatField(max_length=505, unique=False)
    sugar = models.FloatField(max_length=506, unique=False)
    salt = models.FloatField(max_length=507, unique=False)
    store = models.CharField(max_length=508, unique=False)
    nutrition_score = models.CharField(max_length=508, unique=False)
    url_link = models.CharField(max_length=509, unique=False)
    picture_link = models.CharField(max_length=510, unique=False)

    def __str__(self):
        """
        At calling request
        :return: name
        """
        return self.name


class UserLinkToAlimentsTable(models.Model):
    user_id = models.CharField(max_length=200, unique=False)
    aliment_id = models.CharField(max_length=200, unique=False)

    def __str__(self):
        """
        At calling request
        :return: user_id
        """

        return self.user_id
