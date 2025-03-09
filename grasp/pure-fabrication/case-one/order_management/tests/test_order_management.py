import pytest
import datetime

from order_management.application_logic.client_manager import ClientManager
from order_management.application_logic.order_details_manager import OrderDetailsManager
from order_management.data_persistence.address_operations import AddressOperations
from order_management.data_persistence.client_operations import ClientOperations
from order_management.data_persistence.order_operations import OrderOperations
from order_management.data_persistence.payment_operations import PaymentOperations
from order_management.entities.address import Address
from order_management.entities.order import Order
from order_management.entities.payment import Payment
from order_management.entities.product import Product


@pytest.mark.checkout_process
def checkout_process():
    client = ClientManager.create_client_data(identification_type="CC", identification="123456789")
    client_id = ClientOperations.save_client_in_bd(client)

    delivery_address = Address(address_value="Cra 79c # 34 - 56",
                               country="Colombia",
                               city="Medellin",
                               neighborhood="Castilla",
                               department="Antioquia",
                               responsible="Yuly Murillo",
                               address_type="delivery",
                               is_billing_address_same_than_delivery=True,
                               details="Edificio Torre I. Apto 401")
    address_id = AddressOperations.save_address_in_bd(delivery_address)["id"]

    products = [{ "product": Product(product_id=1, name="Camiseta", description="Camiseta rainbow", size="M", price=20000), "amount":1, "discount":0},
                { "product": Product(product_id=2, name="Pantalon", description="Pantalon bota tubo", size="M", price=80000), "amount":1, "discount":0 },
                { "product": Product(product_id=3, name="Chaqueta", description="Chaqueta jean", size="M", price=150000), "amount":1, "discount":0 }]

    gross_value = 0
    for product in products:
        product_gross_value = product["product"].price * product["amount"]
        product_total_discount = product["product"].price * product["discount"]
        product_net_value = product_gross_value - product_total_discount
        gross_value = gross_value + product_net_value
    order = Order(order_id=None,
                  order_date=datetime.date.today(),
                  client=client_id,
                  recipient_name="Yuly Murillo",
                  address=address_id)
    payment = Payment(payment_id=None,
                      payment_type="PSE",
                      discounts=0,
                      charges=19,
                      gross_total=gross_value)
    payment = Payment.calculate_net_value_total(payment)
    payment_id = PaymentOperations.save_payment_in_bd(payment)["id"]
    order.payment_id = payment_id
    order_id = OrderOperations.save_order_in_bd(order)["id"]
    OrderDetailsManager.save_product_details(order_id, products)











