from twilio.rest import Client
from script import get_euromilhoes_results_message

# Twilio credentials
account_sid = 'AC2b82f82d313637b0ff77b731a9d8dd73'
auth_token = '20a524e983897d5d963d9da3898ddf2d'
client = Client(account_sid, auth_token)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+351932822831'

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
