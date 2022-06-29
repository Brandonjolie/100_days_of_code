from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
from_number = os.environ.get("trial_number")
to_number = os.environ.get("to_number")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self) -> None:
        self.messages = []

    def send_messages(self):
        client = Client(account_sid, auth_token)
        for msg in self.messages:
            message = client.messages.create(
                body=msg,
                from_=from_number,
                to=to_number,
            )
