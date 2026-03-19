import serial
import time
from flask import Flask, render_template_string

app = Flask(__name__)

# --- CONFIGURATION ---
SERIAL_PORT = 'COM7' 
BAUD_RATE = 115200

# Storage for readings
data_store = {"accel": "0.00", "pulse_raw": 0, "bpm": "Place Finger", "temp": "0.0", "status": "off"}
ir_buffer = [] 
last_beat_time = time.time()
beat_counts = []

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to Arduino on {SERIAL_PORT}")
except:
    print("Error: Close Arduino Serial Monitor first!")
    exit()

def update_data():
    global last_beat_time, ir_buffer, beat_counts
    if ser.in_waiting > 0:
        try:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if ',' in line:
                parts = line.split(',')
                if len(parts) >= 3:
                    # 1. Update Basic Values
                    data_store["accel"] = parts[0]
                    ir = int(parts[1])
                    data_store["pulse_raw"] = ir
                    data_store["temp"] = parts[2]

                    # 2. Finger Detection Logic
                    if ir < 35000:
                        data_store["bpm"] = "Place Finger"
                        data_store["status"] = "off"
                        ir_buffer = []
                        return

                    data_store["status"] = "on"
                    ir_buffer.append(ir)
                    if len(ir_buffer) > 60: ir_buffer.pop(0)

                    # 3. Beat Detection Math
                    if len(ir_buffer) > 20:
                        avg = sum(ir_buffer) / len(ir_buffer)
                        if ir > avg * 1.0006: 
                            current_time = time.time()
                            duration = current_time - last_beat_time
                            if 0.4 < duration < 1.3: 
                                bpm = 60 / duration
                                beat_counts.append(bpm)
                                if len(beat_counts) > 4: beat_counts.pop(0)
                                data_store["bpm"] = int(sum(beat_counts) / len(beat_counts))
                            last_beat_time = current_time
        except Exception as e:
            print(f"Error: {e}")

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Bio-Sensor Dashboard</title>
    <meta http-equiv="refresh" content="1">
    <style>
        body { font-family: 'Segoe UI'; text-align: center; background: #121212; color: white; padding: 50px; }
        .container { display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; }
        .card { background: #1e1e1e; padding: 25px; border-radius: 20px; width: 220px; border: 1px solid #333; margin: 10px; }
        .label { color: #888; text-transform: uppercase; font-size: 0.7em; letter-spacing: 1px; }
        .value { font-size: 2.2em; font-weight: bold; color: #00d4ff; margin: 10px 0; }
        .bpm-text { color: #ff4757; }
        .temp-text { color: #ffa502; }
        .heart { font-size: 1.5em; display: {{ 'block' if status == 'on' else 'none' }}; animation: beat 0.8s infinite; }
        @keyframes beat { 0% { transform: scale(1); } 50% { transform: scale(1.1); } 100% { transform: scale(1); } }
    </style>
</head>
<body>
    <h1>Multi-Sensor Health Dashboard</h1>
    <div class="container">
        <div class="card">
            <div class="label">Motion</div>
            <div class="value">{{ accel }}<span style="font-size:0.4em"> g</span></div>
        </div>
        <div class="card">
            <div class="label">Body Temp</div>
            <div class="value temp-text">{{ temp }}<span style="font-size:0.4em"> °C</span></div>
        </div>
        <div class="card">
            <div class="label">Heart Rate</div>
            <div class="value bpm-text">{{ bpm }}</div>
            <div class="heart">❤️</div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    update_data()
    return render_template_string(HTML_TEMPLATE, **data_store)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
