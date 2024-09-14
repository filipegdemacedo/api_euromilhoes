import os
from twilio.rest import Client
from script import get_euromilhoes_results_message

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_ACCOUNT_SID')
client = Client(account_sid, auth_token)

from_whatsapp_number = os.getenv('WHATSAPP_FROM_NUMBER')
to_whatsapp_number = os.getenv('WHATSAPP_TO_NUMBER')

def send_whatsapp_message(result_message):
    message = client.messages.create(
        body=get_euromilhoes_results_message(),
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    print(f"Message sent: {message.sid}")

# Example usage: call the function after your script runs
result_message = "Your script analysis result here."
send_whatsapp_message(result_message)
