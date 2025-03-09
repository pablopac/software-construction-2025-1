class Payment:
    net_value = None
    def __init__(self, payment_id, payment_type, discounts, charges, gross_total):
        self.payment_id = payment_id
        self.payment_type = payment_type
        self.discounts = discounts
        self.charges = charges
        self.gross_total = gross_total
        self.net_value = 0


    def calculate_net_value_total(self):
        discounts = self.gross_total*(self.discounts/100)
        charges = self.gross_total*(self.charges/100)
        return  self.gross_total + charges - discounts

