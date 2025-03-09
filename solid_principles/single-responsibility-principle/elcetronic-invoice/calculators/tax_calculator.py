class TaxCalculator:
    """ Calcula los impuestos de una factura. """
    def calculate_taxes(self, subtotal):
        tax_rate = 0.16  # Supongamos un IVA del 16%
        return subtotal * tax_rate



