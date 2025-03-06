from interfaces.payment_processor import PaymentProcessor


class CreditCardProcessor(PaymentProcessor):
    """Procesador de pagos con tarjeta de crédito."""

    def process_payment(self, amount: float) -> str:
        return f"Pago de ${amount:.2f} procesado con Tarjeta de Crédito."
