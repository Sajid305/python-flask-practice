from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/click here to view your data")
def view():
    return "oooooo hi there here is your data"

app.run(debug=True)