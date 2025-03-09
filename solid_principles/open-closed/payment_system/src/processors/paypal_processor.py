from interfaces.payment_processor import PaymentProcessor


class PayPalProcessor(PaymentProcessor):
    """Procesador de pagos con PayPal."""

    def process_payment(self, amount: float) -> str:
        return f"Pago de ${amount:.2f} procesado con PayPal."
