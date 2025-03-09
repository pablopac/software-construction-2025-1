from datetime import datetime
import random

from order_management.entities.client import Client


class ClientManager:

    @staticmethod
    def create_client_data(identification_type, identification):
        phone_number = "({0})-{1}-{2}".format(random.randrange(111, 999),
                                              random.randrange(111, 999),
                                              random.randrange(1111, 9999)
                                              )
        email = "client{0}@{1}".format(datetime.now().strftime("%Y%m%d%H%M%S"), "order.com")

        return Client(identification_type, identification, phone_number, email)

