# InfraSight 🖥️📊  
**A System Intelligence Dashboard built with Flask**

InfraSight is a lightweight but powerful system monitoring dashboard built using Flask, TailwindCSS, and Python libraries like `psutil`. It offers real-time system stats (CPU, memory, disk), API exposure, and a protected admin panel — great for showcasing software, IT, and data engineering skills.

---

## 🌐 Live Demo

🚀 [Visit InfraSight on Render](https://infrasight.onrender.com)

Use the credentials below to access the admin dashboard:

- **Username:** `Md.Rafiquzzaman`  
- **Password:** `admin123`

---

## 🔍 Features

- Real-time CPU, Memory, and Disk usage monitoring using `psutil`
- JSON API endpoint (`/api/system`) for system data
- Admin dashboard protected by session-based login
- Environment variable support for secure credentials
- TailwindCSS for modern, responsive design
- Hosted on [Render](https://render.com)

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Frontend**: HTML, TailwindCSS, Bootstrap  
- **System Monitoring**: `psutil`  
- **Hosting**: Render  
- **Authentication**: Flask Sessions, `.env` secrets

---

## 🚦 Project Structure
InfraSight/
├── app.py                    # Main Flask application with routes and logic
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (secret key, admin credentials)
├── templates/
│   ├── index.html            # Public homepage
│   ├── login.html            # Admin login form
│   └── admin.html            # Admin-only dashboard
├── static/                   # (Optional) Static files like CSS or JS
└── README.md                 # Project documentation

## 🚀 Getting Started (For Local Dev)
🚀 Getting Started

Follow these instructions to run InfraSight locally or test it online.

✅ Live Demo

🌐 Live Site: https://infrasight.onrender.com
🔐 Admin Login:

Username: Md.Rafiquzzaman

Password: admin123

🧑‍💻 Run Locally
1. Clone the Repository
git clone https://github.com/ZCoding82/InfraSight.git
cd InfraSight

2. Create a Virtual Environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Create a .env File

Create a file called .env in the root directory and add:

FLASK_SECRET_KEY=your_strong_secret
ADMIN_USERNAME=Md.Rafiquzzaman
ADMIN_PASSWORD_HASH=scrypt:32768:8:1$rdl2yJQBhrO4VREc$fbf40c73b10fb33be231a2885278d21e4d3491fd51c4de00a9b4d39bdc2240f682e3f69e058544ac5017fb07b1a3d3783c98c03994f5d6ca09a0c20448271fe2


To generate your own hashed password, use Python:

from werkzeug.security import generate_password_hash
print(generate_password_hash("your_password"))

5. Run the App
python app.py

📄 License

This project is licensed under the MIT License – see the LICENSE file for details.

## 🙋‍♂️ About the Developer

Built by Md.Rafiquzzaman
🔧 Flask • Python • Render • VS Code
📫 github.com/ZCoding82
Passionate about IT, system monitoring, and full-stack development.
