from flask import Flask, render_template, request, jsonify
from chatgpt import chat_with_gpt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = chat_with_gpt(message)
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)