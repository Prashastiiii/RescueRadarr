from flask import Flask, render_template, request, jsonify
from chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("user_input")
    response = chatbot.get_response(user_input)
    if not response:
        response = "I don't know the answer to that. What should I respond?"
        return jsonify({"response": response, "learn": True})
    return jsonify({"response": response, "learn": False})

@app.route('/learn_response', methods=['POST'])
def learn_response():
    user_input = request.json.get("user_input")
    new_response = request.json.get("new_response")
    chatbot.learn_response(user_input, new_response)
    return jsonify({"response": "Thank you for teaching me!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
