from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

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

    # Here you can process the data, save it to a database, etc.
    print(f"Received temperature: {temperature}, humidity: {humidity}")

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
