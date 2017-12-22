#!/usr/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

# Temporary data structure to hold information from turn based game
information = [
    {
        'player1': [1,3],
        'player2': [10,10],
    },
    {
        'player1': [1,3,10],
        'player2': [10,10,4],
    }
]

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/get_status', methods=['GET'])
def get_info():
    return jsonify({'status': information})

if __name__ == '__main__':
    app.run(debug=True)
