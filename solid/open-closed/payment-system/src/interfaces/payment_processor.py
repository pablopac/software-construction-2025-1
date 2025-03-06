from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Interfaz para el procesamiento de pagos."""

    @abstractmethod
    def process_payment(self, amount: float) -> str:
        """Método abstracto para procesar el pago."""
        pass
