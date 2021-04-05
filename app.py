from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "It's Alive!!"

app.run()
