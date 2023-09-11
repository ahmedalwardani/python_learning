import smtplib
from twilio.rest import Client

TWILIO_SID = "ACf7dca9c6d5e0a4fb61d80fec0bae5413"
TWILIO_AUTH_TOKEN = "a37c8c69dd10bf0e66f48569d0e708b0"
TWILIO_VIRTUAL_NUMBER = "+19285648193"
TWILIO_VERIFIED_NUMBER = "+16138525167"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "ahmed.alwardani.1995@gmail.com"
MY_PASSWORD = "yrzafyvxammkdtkk"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )










from twilio.rest import Client

TWILIO_SID = "ACf7dca9c6d5e0a4fb61d80fec0bae5413"
TWILIO_AUTH_TOKEN = "a37c8c69dd10bf0e66f48569d0e708b0"
TWILIO_VIRTUAL_NUMBER = "+19285648193"
TWILIO_VERIFIED_NUMBER = "+16138525167"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)