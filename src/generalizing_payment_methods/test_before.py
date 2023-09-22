from .before import CreditCardPayment, PayPalPayment


def test_payment():
    payment1 = CreditCardPayment(100, "1234-5678-9101-1121")
    payment2 = PayPalPayment(200, "email@example.com")

    assert payment1._authorize() == "Authorizing credit card 1234-5678-9101-1121"
    assert payment1.process() == "Processing credit card payment of 100 for card 1234-5678-9101-1121"
    assert payment1.confirm() == "Payment of 100 confirmed"

    assert payment2.process() == "Processing PayPal payment of 200 for email email@example.com"
    assert payment2._send_email_confirmation() == "Sending confirmation email to email@example.com"
    assert payment2.confirm() == "Payment of 200 confirmed"
