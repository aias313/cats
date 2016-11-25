from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACcd6a5fb31a0d7b386953a9bc1a1a4533"
auth_token = "fb81f96ac82b9c61eb814f5badaf59c3"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+15144495275", from_="+15146125319",
                                     body="Hello there!",
                                     media_url=['https://demo.twilio.com/owl.png', 'https://demo.twilio.com/logo.png'])