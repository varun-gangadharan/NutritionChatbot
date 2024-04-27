# app/routes.py
from flask import request, jsonify, render_template
from app import create_app
from app.chatbot_model import get_response  # Assuming get_response handles chatbot functionality

app = create_app()

@app.route('/')
def home():
    # Serve the HTML interface
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['message']
    response = get_response(user_input)  # Process user input through the chatbot model
    return jsonify({'response': response})


@app.route('/test')
def test():
    return "Test page - if you see this, routing works!"