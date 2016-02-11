from twilio.rest import TwilioRestClient
 
# To find these visit https://www.twilio.com/user/account
account_sid = "ACdfd86ae9d14d1932491fb8d18c1bc983"
auth_token = "31999b4fabf7b98ba4491738c9b4c493"
 
client = TwilioRestClient(account_sid, auth_token)
 
for call in client.calls.list():
    print "From: " + call.from_formatted + " To: " + call.to_formatted