class Order:
    def __init__(self,
                 order_id,
                 order_date,
                 client,
                 payment_id,
                 recipient_name,
                 address):
        self.order_id = order_id
        self.order_date = order_date
        self.client = client
        self.payment_id = payment_id
        self.recipient_name = recipient_name
        self.address = address



