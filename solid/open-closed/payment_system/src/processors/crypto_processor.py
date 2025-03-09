from interfaces.payment_processor import PaymentProcessor


class CryptoProcessor(PaymentProcessor):
    """Procesador de pagos con Criptomonedas."""

    def process_payment(self, amount: float) -> str:
        return f"Pago de ${amount:.2f} procesado con Criptomonedas."
