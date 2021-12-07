from twilio.rest import Client


def sendotp(otpreci):
    account_sid = 'ACe8caad8112e2135294377d739ce3e9b9'
    auth_token = 'd40a4a4769a9e56e5a17e1b5b3664930'
    client = Client(account_sid, auth_token) 
    msg='OTP for Login : ' + str(otpreci)
    
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body= msg ,
    to='whatsapp:+918421296860'
    )
    



