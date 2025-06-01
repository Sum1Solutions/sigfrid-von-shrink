from flask import Flask, render_template, request, jsonify, session
from chatgpt import chat_with_gpt
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev_secret_key')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    # Initialize conversation history if not present
    if 'history' not in session:
        session['history'] = []
    # Append user message
    session['history'].append({'role': 'user', 'content': message})
    # Call chatgpt with full history
    response = chat_with_gpt(session['history'])
    # Append AI response
    session['history'].append({'role': 'assistant', 'content': response})
    session.modified = True
    return jsonify({'message': response})

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('history', None)
    return jsonify({'message': 'Conversation history reset.'})

if __name__ == '__main__':
    app.run(debug=True)