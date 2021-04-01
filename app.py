# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import psycopg2
import os
import database

app = Flask(__name__)
# Eliminate CORS issue.
CORS(app)

@app.route('/waitlist', methods=['POST'])
def post_waitlist():
    param = request.get_json()
    print(param)
    
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        database.add_email(param)
        return jsonify({
            "Message": f"Welcome {param.get('email')} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no email found, please send email."
        })

# A welcome message to test our server
@app.route('/')
def index():

    return "<h1>Dude, wyd? Go somewhere else lmao... but if you need taxes done we got ur back.. btw we're planning on rolling out the rest of our bank soon. Wouldn't it make a lot of sense if your bank offered to do your taxes? And budget? And like way more than your bank now does? Yea we know.</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
