from order_management.application_logic.client_manager import ClientManager
from order_management.application_logic.order_manager import OrderManager
from order_management.application_logic.payment_manager import PaymentManager

from order_management.data_persistence.order_operations import OrderOperations
from order_management.entities.status import Status


class CheckoutProcessor:
    @staticmethod
    def checkout_order(identification_type, identification, products, payment_type, discounts, charges, gross_value):
        status = Status("Pending", "This is a new order.")
        client = ClientManager.create_client(identification_type, identification)
        payment = PaymentManager.create_payment(payment_type, discounts, charges, gross_value)
        order = OrderManager.create_order(status, client, payment, products)
        OrderOperations.save_order_in_bd(order)







