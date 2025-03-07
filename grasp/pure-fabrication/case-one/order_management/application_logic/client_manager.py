import datetime
import random

from order_management.entities.client import Client


class ClientManager:

    @staticmethod
    def create_client(identification_type, identification):
        phone_number = "({0})-{1}-{2}".format(random.randrange(111, 999),
                                              random.randrange(111, 999),
                                              random.randrange(1111, 9999)
                                              )
        email = datetime.date.today()

        return Client(identification_type, identification, phone_number, email)
