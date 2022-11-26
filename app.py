from flask import Flask, jsonify
import psutil
from psutil._common import bytes2human


app = Flask(__name__)

api_key = '1234567890'
@app.route('/api/v1/health/api_key=1234567890', methods=['GET'])
def get_system_info():
    ram = psutil.virtual_memory()
    cpu_temp  = psutil.sensors_temperatures(fahrenheit=False)
    load_avg = psutil.getloadavg()
    print(ram, cpu_temp, load_avg)
    return jsonify(psutil.sensors_temperatures(fahrenheit=False), psutil.getloadavg(), psutil.virtual_memory(), psutil.disk_usage('/'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))
