class InvoiceProcessor:
    #"""Procesa la generación y manejo de facturas."""
    def __init__(self, validator, storage, notifier):
        self.validator = validator
        self.storage = storage
        self.notifier = notifier

    def process_invoice(self, fiscal_data, invoice, email):
        if self.validator.validate_fiscal_data(fiscal_data):
            if self.storage.store_invoice(invoice):
                return self.notifier.send_invoice_notification(email, invoice)
        return False
