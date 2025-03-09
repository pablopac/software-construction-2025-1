from calculators.tax_calculator import TaxCalculator
from generators.invoice_generator import InvoiceGenerator
from senders.invoice_sender import InvoiceSender

def main():
    items = [
        {'price': 120.00, 'quantity': 2},
        {'price': 45.50, 'quantity': 3}
    ]

    tax_calculator = TaxCalculator()
    invoice_generator = InvoiceGenerator(tax_calculator)
    invoice = invoice_generator.generate_invoice(items)

    invoice_sender = InvoiceSender()
    if invoice_sender.send_invoice(invoice):
        print("Factura enviada con Exito.")

if __name__ == "__main__":
    main()

