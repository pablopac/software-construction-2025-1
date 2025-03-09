from order_management.data_persistence.order_operations import OrderOperations

class OrderManager:

    def __init__(self, order):
        self.order = order

    def store_order_in_bd(self):
        return OrderOperations.save_order_in_bd(self.order)



