from flask import Flask, jsonify
import psutil, time, os, requests
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
api_key = os.getenv("API_KEY")
@app.route('/')
def homepage():
    return "Hi"


@app.route(f'/api/ubuntu2204/api_key={api_key}', methods=['GET'])
def get_system_info():
    ram = psutil.virtual_memory()
    cpu_temp  = psutil.sensors_temperatures(fahrenheit=False)
    load_avg = psutil.getloadavg()
    print(ram, cpu_temp, load_avg)
    return jsonify(psutil.sensors_temperatures(fahrenheit=False), psutil.getloadavg(), psutil.virtual_memory(), psutil.disk_usage('/'), time.time())

@app.route(f'/api/shelly/shellyplugs/api_key={api_key}', methods=['GET'])
def get_shelly_plug_s():
    response = requests.get('http://192.168.180.45/status')
    return response.json()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))
