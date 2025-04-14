from twilio.rest import Client
import os

TWILIO_SID = "TWILIO_SID"
TWILIO_AUTH_TOKEN = "TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "TWILIO_PHONE_NUMBER"
ADMIN_PHONE_NUMBER = "ADMIN_PHONE_NUMBER"

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_alert(species, category, timestamp, location):
    """Sends an SMS alert for Harmful and Lethal animal detections."""
    if category in ["Harmful", "Lethal"]:
        message_body = (
            f"ALERT: {species} detected!\n"
            f"Category: {category}\n"
            f"Time: {timestamp}\n"
            f"Location: {location}\n"
            f"Google Maps: https://www.google.com/maps/search/?api=1&query={location}"
        )
        try:
            message = client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER,
                to=ADMIN_PHONE_NUMBER
            )
            print(f"Alert sent: {message.sid}")
        except Exception as e:
            print(f"Failed to send alert: {e}")
