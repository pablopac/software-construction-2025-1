import random

from order_management.entities.payment import Payment


class PaymentManager:

    @staticmethod
    def create_payment_id():
        return random.randrange(11111111, 99999999)

    def create_payment(self, payment_type, discounts, charges, gross_value):
        payment_id = self.create_payment_id()
        return Payment(payment_id, payment_type, discounts, charges, gross_value)
