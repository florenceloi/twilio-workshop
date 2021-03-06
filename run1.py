from flask import Flask, render_template
from twilio.util import TwilioCapability
 
app = Flask(__name__)
 
@app.route('/client', methods=['GET', 'POST'])
def client():
    """Respond to incoming requests."""
 
    account_sid = "ACdfd86ae9d14d1932491fb8d18c1bc983"
    auth_token = "31999b4fabf7b98ba4491738c9b4c493"
 
    # This is a special Quickstart application sid - or configure your own
    # at twilio.com/user/account/apps
    application_sid = "APabe7650f654fc34655fc81ae71caa3ff"
 
    capability = TwilioCapability(account_sid, auth_token)
    capability.allow_client_outgoing(application_sid)
    token = capability.generate()
 
    return render_template('client.html', token=token)
 
if __name__ == "__main__":
    app.run(debug=True)