import os
from twilio.rest import Client
from script import get_euromilhoes_results_message

def send_whatsapp_message(result_message):
    # Fetch credentials from environment variables
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    
    if not account_sid or not auth_token:
        raise ValueError("Twilio credentials are not set properly")

    client = Client(account_sid, auth_token)

    from_whatsapp_number = os.getenv('WHATSAPP_FROM_NUMBER')
    to_whatsapp_number = os.getenv('WHATSAPP_TO_NUMBER')

    if not from_whatsapp_number or not to_whatsapp_number:
        raise ValueError("WhatsApp numbers are not set properly")

    message = client.messages.create(
        body=result_message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    print(f"Message sent successfully with SID: {message.sid}")

result_message = get_euromilhoes_results_message()

send_whatsapp_message(result_message)