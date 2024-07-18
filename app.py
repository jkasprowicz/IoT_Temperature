from flask import Flask, request, jsonify, render_template
from models import db, TemperatureData

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Ensure tables are created before the first request
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    data = TemperatureData.query.order_by(TemperatureData.timestamp.desc()).all()
    return render_template('index.html', data=data)

@app.route('/temperature', methods=['POST'])
def receive_temperature():
    data = request.get_json()
    
    # Print the raw data to debug
    print(f"Received raw data: {data}")
    
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    
    temperature = data.get('temperatura')
    humidity = data.get('humidade')
    
    if temperature is None or humidity is None:
        return jsonify({"error": "Missing data"}), 400

    # Save the data to the database
    new_data = TemperatureData(temperature=temperature, humidity=humidity)
    db.session.add(new_data)
    db.session.commit()

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
