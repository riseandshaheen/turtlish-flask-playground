print("Starting Flask app...")
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import traceback
from turtlish import draw_with_turtle_to_base64
import matplotlib
matplotlib.use('Agg')

# Assuming the Turtlish and related functions are defined as above and imported here

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests for frontend communication

@app.route("/")
def start():
    return "Turtlish flask server is Running"

@app.route('/draw', methods=['POST'])
def draw():
    try:
        data = request.get_json()
        user_code = data.get("code", "")

        if not user_code:
            return jsonify({"error": "No code provided."}), 400

        # Generate the image as base64 string
        base64_img = draw_with_turtle_to_base64(user_code)
        return jsonify({"image": base64_img}), 200

    except Exception as e:
        logging.error(f"Error executing code: {e}\n{traceback.format_exc()}")
        error_message = f"While executing code: {e}"
        return jsonify({"error": error_message}), 500

