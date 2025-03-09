from services.payment_service import PaymentService
from processors.credit_card_processor import CreditCardProcessor
from processors.paypal_processor import PayPalProcessor
from processors.crypto_processor import CryptoProcessor


class PaymentController:
    """Controlador para manejar solicitudes de pago."""

    def process_payment(self, method: str, amount: float) -> str:
        """Procesa el pago basado en el método seleccionado."""

        processors = {
            "credit_card": CreditCardProcessor(),
            "paypal": PayPalProcessor(),
            "crypto": CryptoProcessor()
        }

        if method not in processors:
            return "Método de pago no soportado."

        service = PaymentService(processors[method])
        return service.process(amount)
