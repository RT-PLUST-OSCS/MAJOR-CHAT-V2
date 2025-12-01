from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# تخزين الرسائل (في تطبيق حقيقي استخدم قاعدة بيانات)
messages = []

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    message = {
        'text': data['message'],
        'sender': data['sender'],
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }
    messages.append(message)
    return jsonify({'status': 'success'})

@app.route('/get_messages')
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)