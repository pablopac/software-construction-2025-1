#Single Responsibility Principle(SRP) aplicado a un sistema de facturación electrónica  
#Se manejaria el tener múltiples responsabilidades

#InvoiceGenerator: Responsable de crear la estructura de la factura.
#TaxCalculator: Encargada de calcular los impuestos de la factura.
#InvoiceSender: Maneja el envío de la factura a través de un servicio web.

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

