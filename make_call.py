# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
account_sid = "ACdfd86ae9d14d1932491fb8d18c1bc983"
auth_token = "31999b4fabf7b98ba4491738c9b4c493"
client = TwilioRestClient(account_sid, auth_token)

# Make the call
call = client.calls.create(to="+14083867850",  # Any phone number
                           from_="+18316121344",    # Must be a valid Twilio number
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print call.sid
