from order_management.data_persistence.status_operations import StatusOperations

class StatusManager:

    def __init__(self, order_status):
        self.order_status = order_status

    def update_order_status(self):
        StatusOperations.update_order_status_in_bd(self.order_status)


