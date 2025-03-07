from twilio.rest import Client
import os

# ✅ Twilio Credentials (Replace with your actual credentials)
ACCOUNT_SID = "ACd7396bd98041c33369dbeeba5b016c6c"
AUTH_TOKEN = "c97e16d20dac62f4ab28d9ad8e8eb797"
TO_NUMBER = "+919580951150"  # ✅ Your verified phone number
FROM_NUMBER = "+18786453317"  # ✅ Your Twilio number

def sendSms():
    try:
        print("📨 Attempting to send SMS to:", TO_NUMBER)  # Debugging log

        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body="🚨 Intrusion Alert! A person has been detected!",
            from_=FROM_NUMBER,
            to=TO_NUMBER  
        )

        print("✅ SMS Sent! Message SID:", message.sid)  # Log success
        return True  # ✅ Indicate SMS was sent successfully

    except Exception as e:
        print("⚠️ Error sending SMS:", e)  # Log the error
        return False  # ❌ Indicate SMS failed

# ✅ Test by running this script directly
if __name__ == "__main__":
    sendSms()


