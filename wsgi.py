from flask import Flask
import os

application = Flask(__name__)

@application.route("/")
def hello():
    message = os.environ.get('message','none')
    return str(message)

if __name__ == "__main__":
    application.run()
