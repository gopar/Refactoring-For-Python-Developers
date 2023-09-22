class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        return f"Processing payment of {self.amount}"

    def confirm(self):
        return f"Payment of {self.amount} confirmed"


class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):
        return f"Processing credit card payment of {self.amount} for card {self.card_number}"

    def authorize(self):
        return f"Authorizing credit card {self.card_number}"


class PayPalPayment(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):
        return f"Processing PayPal payment of {self.amount} for email {self.email}"

    def send_email_confirmation(self):
        return f"Sending confirmation email to {self.email}"
