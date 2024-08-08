from flask import Flask 
import requests

app = Flask(__name__)

API_URL = 'http://127.0.0.1:5000/api/livros'

@app.route('/')
def index():
    response = requests.get(API_URL)
    if response.status_code == 200:
        livros = response.json()
    else:
        livros = []

if __name__ == '__main__':
    app.run(port=5001, debug=True, )