class OrderDetails:

    def __init__(self,
                 order_id,
                 product_id,
                 discount,
                 amount,
                 gross_value,
                 net_value
                 ):
        self.order_id = order_id
        self.product_id = product_id
        self.discount = discount
        self.amount = amount
        self.gross_value = gross_value
        self.net_value = net_value



