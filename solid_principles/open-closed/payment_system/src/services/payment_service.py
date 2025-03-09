from interfaces.payment_processor import PaymentProcessor


class PaymentService:
    """Servicio que gestiona el procesamiento de pagos."""

    def __init__(self, processor: PaymentProcessor):
        """Recibe una instancia de PaymentProcessor (inyección de dependencias)."""
        self.processor = processor

    def process(self, amount: float) -> str:
        """Procesa el pago con el método seleccionado."""
        return self.processor.process_payment(amount)
