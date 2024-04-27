# app/routes.py
from app import app
from flask import render_template, request, jsonify
from app.chatbot_model import get_chatbot_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    response = get_chatbot_response(user_input)
    return jsonify({'response': response})