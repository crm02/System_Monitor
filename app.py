from flask import Flask, render_template, jsonify
import webbrowser
import threading
import psutil
import time

app = Flask(__name__)
port = 5000 # default flask port
last_disk = psutil.disk_io_counters()
last_disk_time = time.time()

last_net = psutil.net_io_counters()
last_time = time.time()




psutil.cpu_percent(percpu=False)

def get_cpu_per():
    psutil.cpu_percent()  
    time.sleep(0.1)  

    return psutil.cpu_percent()  

def get_ram():
    return psutil.virtual_memory().percent

def open_browser():
    webbrowser.open_new(f"http://127.0.0.1:{port}")

def get_disk_activity():
    global last_disk, last_disk_time
    current_disk = psutil.disk_io_counters()
    current_time = time.time()
    elapsed = current_time - last_disk_time
    
    if elapsed <= 0:
        return 0.0
    
    
    read_speed = (current_disk.read_bytes - last_disk.read_bytes) / elapsed
    write_speed = (current_disk.write_bytes - last_disk.write_bytes) / elapsed
    
    last_disk = current_disk
    last_disk_time = current_time
    

    total_activity = (read_speed + write_speed) / (100 * 1024 * 1024)  
    return min(total_activity * 100, 100) 

def get_network_speed():
    global last_net, last_time
    current_net = psutil.net_io_counters()

    current_time = time.time()

    elapsed = current_time - last_time

    if elapsed <= 0:
        return 0.0, 0.0

    upload_speed = (current_net.bytes_sent - last_net.bytes_sent) / elapsed
    download_speed = (current_net.bytes_recv - last_net.bytes_recv) / elapsed

    last_net = current_net
    last_time = current_time

    #return KB/s
    return upload_speed / 1024, download_speed / 1024



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/metrics")
def metrics():
    cpu = get_cpu_per()

    ram = get_ram()

    disk = get_disk_activity()  

    up, down = get_network_speed()

    return jsonify({
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "net_up": up,
        "net_down": down
    })



if __name__ == "__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True, port=port)
    