import datetime
import random

from order_management.entities.order import Order


class OrderManager:

    def __init__(self, order_status, client, payment, products):
        self.order_id = self.create_order_id()
        self.order_date = datetime.date.today()
        self.order_status = order_status
        self.client = client
        self.payment = payment
        self.products = products

    @staticmethod
    def create_order_id():
        return random.randrange(11111111, 99999999)

    @staticmethod
    def create_order(order_status, client, payment, products):
        return Order(order_status, client, payment, products)


