class InvoiceGenerator:
    #""" Genera una factura con detalles y culculos de impuestos. """
    def __init__(self, tax_calculator):
        self.tax_calculator = tax_calculator

    def generate_invoice(self, items):
        subtotal = sum(item['price'] * item['quantity'] for item in items)
        taxes = self.tax_calculator.calculate_taxes(subtotal)
        total = subtotal + taxes
        return {
            'items': items,
            'subtotal': subtotal,
            'taxes': taxes,
            'total': total
        }