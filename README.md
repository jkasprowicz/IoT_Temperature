# IoT Temperature Tracker with ESP-01 and DHT22

This project involves setting up an IoT temperature and humidity tracker using an ESP-01 module with a DHT22 sensor. The ESP-01 is programmed to measure environmental data and send it to a server for further processing.

## Components Used
- **ESP-01 Module:** WiFi-enabled microcontroller based on the ESP8266 chip.
- **DHT22 Sensor:** Provides temperature and humidity readings.
- **Jumper Wires:** Used for connecting components.
- **USB to TTL Adapter:** Configures the ESP-01 module using Arduino IDE.
- **AAA Battery Pack:** Supplies power to the IoT device.

## Workflow
1. **Configuration with Arduino IDE:**
   - The ESP-01 module is configured using Arduino IDE to read data from the DHT22 sensor.
   - It connects to a WiFi network and sends measurements to a designated server endpoint.

2. **Hardware Setup:**
   - The DHT22 sensor is connected to the ESP-01 module using jumper wires.
   - The setup is powered by a AAA battery pack, providing portability and flexibility.

3. **Server Configuration:**
   - An Oracle Cloud instance is provisioned to host a Flask application.
   - This application receives data sent by the ESP-01 module, processes it, and stores it in a database.

4. **Application Deployment:**
   - The Flask application is deployed on the Oracle Cloud instance to handle incoming sensor data.
   - It provides endpoints to receive POST requests containing temperature and humidity measurements.

## Deployment Steps
- **Setup ESP-01 with DHT22:**
  - Connect DHT22 to ESP-01 using jumper wires.
  - Flash the ESP-01 using Arduino IDE to include WiFi connection and sensor reading logic.

- **Oracle Cloud Instance:**
  - Create an Always Free tier instance on Oracle Cloud.
  - Configure the instance to run a Flask application that listens for POST requests from the ESP-01.

- **GitHub Repository:**
  - The project is version-controlled using Git.
  - Codebase includes Arduino sketches for ESP-01, Flask application for Oracle Cloud, and documentation.

## Usage
- **Local Testing:**
  - Test the ESP-01 setup locally using a USB to TTL adapter.
  - Verify temperature and humidity readings on the Arduino IDE serial monitor.

- **Deployment to Oracle Cloud:**
  - Push changes to the GitHub repository.
  - Clone the repository onto the Oracle Cloud instance and deploy the Flask application.

---
