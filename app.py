from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import psutil
import datetime
import os
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "fallback_secret_key")  # 🔐 Set this in production!

# Admin credentials (from environment)
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD_HASH = os.environ.get("ADMIN_PASSWORD_HASH", generate_password_hash("password123"))

# ────────────────────────────────
# ROUTES
# ────────────────────────────────

# Homepage
@app.route("/")
def dashboard():
    return render_template("index.html")

# System info API
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

# Admin Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
            session["logged_in"] = True
            return redirect(url_for("admin_dashboard"))
        return render_template("login.html", error="Invalid username or password.")
    return render_template("login.html")

# Admin Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# Admin-only dashboard
@app.route("/admin")
def admin_dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return render_template("admin.html", cpu=cpu, mem=mem, disk=disk)

# ────────────────────────────────
# Run Server (Local Only)
# ────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
