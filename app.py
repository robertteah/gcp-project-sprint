from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_universe():
    return 'Hello, Universe, Simple Flask application!'