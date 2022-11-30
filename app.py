from flask import Flask
app = Flask(__name__)
@app.route('/')
def Beat_Navy():
    return 'Beat Navy!!'

