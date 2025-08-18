from flask import Flask, render_template, jsonify
import psutil
import datetime

app = Flask(__name__)

# Route: Main Dashboard Page
@app.route("/")
def dashboard():
    return render_template("index.html")

# Route: API for System Information
@app.route("/api/system")
def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    system_data = {
        "cpu_percent": cpu_percent,
        "memory": {
            "total": memory.total,
            "used": memory.used,
            "percent": memory.percent
        },
        "disk": {
            "total": disk.total,
            "used": disk.used,
            "percent": disk.percent
        },
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return jsonify(system_data)

# Entry point
if __name__ == "__main__":
    app.run(debug=True)
