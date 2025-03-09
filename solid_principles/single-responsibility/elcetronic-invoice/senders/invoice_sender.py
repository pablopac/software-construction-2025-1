class InvoiceSender:
    #""" Envia la factura generada a un servicio web. """
    def send_invoice(self, invoice):
       
        print("Enviando factura al servicio web...")
        print(invoice)
        # Simularemos que el envio fue exitoso.
        return True