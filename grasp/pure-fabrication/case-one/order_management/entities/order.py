class Order:
    def __init__(self,
                 order_id,
                 order_date,
                 order_status,
                 client,
                 payment):
        self.order_id = order_id
        self.order_date = order_date
        self.order_status = order_status
        self.client = client
        self.payment = payment



