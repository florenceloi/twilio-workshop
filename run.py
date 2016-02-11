from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

callers = {
    "+14083867850": "Floyster",
}


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()

    if from_number in callers:
        resp.say("Hello " + callers[from_number])
        resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
    else:
        resp.say("Hello cray cray")

    with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
        g.say("""To speak to a real monkey, press 1.
                 Press 2 to record your own monkey howl.
                 Press any other key to start over.""")

    return str(resp)


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    """Handle key press from a user."""

    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = twilio.twiml.Response()
        # Dial (310) 555-1212 - connect that number to the incoming caller.
        resp.dial("+13105551212")
        # If the dial fails:
        resp.say("The call failed, or the remote party hung up. Goodbye.")

        return str(resp)

    elif digit_pressed == "2":
        resp = twilio.twiml.Response()
        resp.say("Record your monkey howl after the tone.")
        resp.record(maxLength="30", action="/handle-recording")

        return str(resp)

    # If the caller pressed anything but 1, redirect them to the homepage.
    else:
        return redirect("/")


@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""

    recording_url = request.values.get("RecordingUrl", None)

    resp = twilio.twiml.Response()
    resp.say("Thanks for howling... take a listen to what you howled.")
    resp.play(recording_url)
    resp.say("Goodbye.")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)