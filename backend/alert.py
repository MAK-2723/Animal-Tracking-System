from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
ADMIN_PHONE_NUMBER = os.getenv("ADMIN_PHONE_NUMBER")

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