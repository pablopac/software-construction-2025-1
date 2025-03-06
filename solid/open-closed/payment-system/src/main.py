from controllers.payment_controller import PaymentController

if __name__ == "__main__":
    controller = PaymentController()

    print(controller.process_payment("credit_card", 100.00))
    print(controller.process_payment("paypal", 250.50))
    print(controller.process_payment("crypto", 500.75))
    print(controller.process_payment("bank_transfer", 300.00))
