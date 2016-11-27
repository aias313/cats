from flask import Flask, request, redirect, render_template, url_for
import twilio.twiml
import urllib
from twilio.rest import TwilioRestClient
import datetime
# put your own credentials here
ACCOUNT_SID = "ACcd6a5fb31a0d7b386953a9bc1a1a4533"
AUTH_TOKEN = "fb81f96ac82b9c61eb814f5badaf59c3"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        number = request.form['number']
        sender = request.form['sender']
        # if datetime.weekday() == 5:
        #     greeting = "happy caturday"
        message = client.messages.create(to="+1"+number, from_="+15146125319",
                                         body="Hello there!",
                                         media_url=['http://cataas.com/cat/says/hello%20from%20'+sender])

        return render_template('success.html', number=number)

    return render_template('index.html')
# @app.route("/sms", methods=['GET', 'POST'])
# def index():
# def hello_monkey():
#
#     if request.method =='POST':
#         number = request.form['number']
#         sender = request.form['sender']
#         note=request.form['note']
#         # send()
#         return render_template('form.html')
#         # return redirect(url_for("success"))
#     else:
#         sent_msg = request.values.get('Body', None)
#         media_url = "http://cataas.com/cat/says/" + urllib.parse.quote(sent_msg)
#         text = "Happy Caturday"
#
#     resp = twilio.twiml.Response()
#
#     with resp.message(text) as m:
#         m.media(media_url)
#     return str(resp)
#
# @app.route('/success')
# def success():
#     return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
