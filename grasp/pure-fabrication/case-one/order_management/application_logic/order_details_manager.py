from order_management.data_persistence.order_details_operations import OrderDetailsOperations
from order_management.entities.order_details import OrderDetails


class OrderDetailsManager:

    @staticmethod
    def save_product_details(order_id, products):

        try:
            for product in products:
                gross_value = product["product"].price*product["amount"]
                total_discount = product["product"].price*product["discount"]
                net_value = gross_value - total_discount
                order_detail = OrderDetails(order_id,
                                            product["product"].product_id,
                                            product["discount"],
                                            product["amount"],
                                            gross_value,
                                            net_value)
                OrderDetailsOperations.save_order_details_in_bd(order_detail)
        except:
            OrderDetailsOperations.rollback_order_detail_operation()



