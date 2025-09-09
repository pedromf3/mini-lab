from flask import Flask, render_template, request, jsonify
from global_weather.wxtracker import get_weather_data
from password_generator.gen_password import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# ---- APIs ----
@app.route('/api/weather', methods=['POST'])
def api_weather():
    location = request.json.get("location")
    try:
        data = get_weather_data(location)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/password', methods=['POST'])
def api_password():
    length = request.json.get("length", 12)
    try:
        pwd = generate_password(length)
        return jsonify({"password": pwd})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
