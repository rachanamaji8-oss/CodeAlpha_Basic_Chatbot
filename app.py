from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hi! 👋 How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm fine, thanks for asking! 😊 How about you?"
    elif 'bye' in user_input or 'goodbye' in user_input:
        return "Goodbye! Have a great day! 👋"
    elif 'what is your name' in user_input:
        return "I'm Chatbuddy 🤖"
    elif 'time' in user_input:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return f"The current time is {current_time} 🕒"
    elif 'weather' in user_input:
        return "I'm not connected to the internet, but I hope the weather is great where you are! ☀️🌧️"
    elif 'thank you' in user_input or 'thanks' in user_input:
        return "You're welcome! 😊"
    elif 'help' in user_input:
        return "Sure! You can ask me about my name, time, weather, or just say hello 👋"
    else:
        return "Sorry, I don't understand that. 😕"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.form['msg']
    bot_response = get_bot_response(user_input)
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)