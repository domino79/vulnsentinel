# VulnSentinel – Vulnerability Scanner / Log Analyzer

🔐 A lightweight cybersecurity tool that scans server logs to detect and flag potential threats in real time. Built with Python and Flask, VulnSentinel helps IT professionals identify suspicious patterns such as SQL injections, brute force attempts, and XSS attacks.

## 🚀 Features

- ✅ Parses Apache, Nginx, and generic server logs
- ✅ Detects:
  - SQL Injection attempts
  - Cross-Site Scripting (XSS)
  - Brute force login attempts
  - Suspicious IP access patterns
- ✅ Real-time monitoring via Flask-based web dashboard
- ✅ Customizable alert rules

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Security Logic**: Regex pattern matching, log parsing, threat flagging  
- **Frontend**: HTML/CSS, Bootstrap (Flask templates)  
- **Optional Add-ons**: Log file upload, alert notification system

---

## 📂 Project Structure

vulnsentinel/ │ ├── app.py # Flask app entry point ├── parser/ │ └── log_parser.py # Log reading & pattern matching logic ├── templates/ │ └── dashboard.html # Frontend HTML for results ├── static/ │ └── style.css # Styling (Bootstrap or custom) ├── samples/ │ └── apache_log_sample.txt # Sample log file ├── requirements.txt # Dependencies └── README.md

---

## 🧪 How to Use

1. **Clone the repository**
```bash
git clone https://github.com/domino79/vulnsentinel.git
cd vulnsentinel

2. Create a virtual environment & install dependencies
python -m venv env
source env/bin/activate  # or `env\\Scripts\\activate` on Windows
pip install -r requirements.txt

3. Run the Flask app
python app.py

4. Visit the dashboard
http://127.0.0.1:5000

Skills Demonstrated
✅ Certified Information Systems Auditor (CISA)

✅ (ISC)² Cybersecurity Techniques

✅ Python scripting for threat detection

✅ Flask web development

✅ Secure log analysis

License
MIT License – free for public use and contribution.

Contributions
Issues and pull requests are welcome. Let’s make VulnSentinel smarter together!

---

