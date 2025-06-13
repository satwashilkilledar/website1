from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
  return "welcome to the flask app-Bhai"

app.run(host="0.0.0.0", port=3000, debug=True)
