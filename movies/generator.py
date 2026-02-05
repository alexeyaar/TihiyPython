import random
import string
from faker import Faker
faker = Faker()

class Generator:

    @staticmethod
    def generate_name():
        name_random = faker.first_name()
        return name_random

    @staticmethod
    def generate_lastname():
        lastname_random = faker.last_name()
        return lastname_random

    @staticmethod
    def generate_price():
        price_random = faker.random_int()
        return price_random

    @staticmethod
    def generate_datebook():
        date = {
            "checkin": faker.date(),
            "checkout":faker.date()
        }
        return date

    @staticmethod
    def generate_additionalneeds():
        stribg = faker.text()
        return stribg