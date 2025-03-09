class Address:

    def __init__(self,
                 address_value,
                 country,
                 city,
                 neighborhood,
                 department,
                 responsible,
                 address_type,
                 is_billing_address_same_than_delivery,
                 details
                 ):
        self.address_value = address_value
        self.country = country
        self.city = city
        self.neighborhood = neighborhood
        self.department = department
        self.responsible = responsible
        self.address_type = address_type,
        self.is_billing_address_same_than_delivery = is_billing_address_same_than_delivery
        self.details = details



