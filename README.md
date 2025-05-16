# 🔍 Nmap Web Automation Tool

A web-based tool built using **Flask** that allows users to run `nmap` scans on any domain or IP address directly from a simple web interface — no command line needed!

---

## 🚀 Features

- 🖥️ Easy-to-use web interface
- ⚡ Run `nmap -sV` scans
- 📋 Display results directly in browser
- 💾 Optional logging or output saving
- 🔐 Built with cybersecurity in mind

---

## 🛠️ Tech Stack

- Python 3.10
- Flask
- Nmap (system installed)
- Kali Linux (or any Linux distro)
- Pipenv (for managing dependencies)

---

## 📦 Setup Instructions (Kali Linux)

```bash
# Install pipenv and Flask
sudo apt install python3-pip -y
pip install pipenv
pipenv install flask
pipenv shell

# Create folder structure
mkdir -p nmap-webtool/templates
cd nmap-webtool

# Add your files here
nano app.py
nano templates/index.html

# Run the app
python app.py

