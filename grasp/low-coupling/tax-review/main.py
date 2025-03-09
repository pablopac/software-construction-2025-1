#Low Coupling se refiere a reducir las dependencias entre las clases para aumentar 
#la reusabilidad y facilitar el mantenimiento del sistema.

#Low Coupling en un sistema de facturación electrónica, En el ejemplo involucra la
# interacción con una base de datos para almacenar los detalles de las facturas y la comunicación 
# con un sistema externo para validar datos fiscales

#Validación Fiscal: Antes de generar la factura, es necesario validar ciertos datos fiscales del cliente 
# (como el número de identificación fiscal) con una entidad gubernamental.

#Almacenamiento de Facturas: Después de generar la factura, esta debe ser almacenada en una base de datos.

#Notificación al Cliente: Una vez almacenada la factura, el sistema debe notificar al cliente por 
# correo electrónico.

from services.fiscal_validator import FiscalValidator
from services.invoice_storage import InvoiceStorage
from services.email_notifier import EmailNotifier
from processors.invoice_processor import InvoiceProcessor

def main():
    validator = FiscalValidator()
    storage = InvoiceStorage()
    notifier = EmailNotifier()
    processor = InvoiceProcessor(validator, storage, notifier)

    fiscal_data = {"id": "ABC123456789"}
    invoice_data = {"id": "INV10001", "amount": 2000}
    email = "cliente@example.com"

    if processor.process_invoice(fiscal_data, invoice_data, email):
        print("Proceso de facturación completado exitosamente.")
    else:
        print("Error en el proceso de facturación.")

if __name__ == "__main__":
    main()
