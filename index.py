from flask import Flask, request, jsonify

app = Flask(__name__)

# Get user preference request
@app.route('/get_preference', methods=['GET'])
def get_preference():
    user_id = request.args.get('user_id')
    return jsonify({"user_id": user_id})

# Receive user preference and send back to PHP
@app.route('/set_preference', methods=['POST'])
def set_preference():
    data = request.json
    user_id = data.get('user_id')
    theme = data.get('theme')
    background_color = data.get('background_color')
    
    if not user_id or not theme or not background_color:
        return jsonify({"error": "Missing data"}), 400
    
    return jsonify({"user_id": user_id, "theme": theme, "background_color": background_color})

# Root route to display a message
@app.route('/')
def home():
    return "Flask Microservice for Theme Preferences is Running!"

if __name__ == '__main__':
    app.run(debug=True)