from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process(self):
        pass

    def confirm(self):
        return f"Payment of {self.amount} confirmed"


class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        return self._authorize_and_process()

    def _authorize_and_process(self):
        self._authorize()
        return f"Processing credit card payment of {self.amount} for card {self.card_number}"

    def _authorize(self):
        return f"Authorizing credit card {self.card_number}"


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):
        return self._process_and_email()

    def _process_and_email(self):
        self._send_email_confirmation()
        return f"Processing PayPal payment of {self.amount} for email {self.email}"

    def _send_email_confirmation(self):
        return f"Sending confirmation email to {self.email}"
