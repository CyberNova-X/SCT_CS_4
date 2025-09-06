# SCT_CS_4 – CLI Keylogger (Safe Demo Tool)

**SkillCraft Cyber Security Internship – Task 4**

---

## 🔹 Overview
This project is a **Command-Line Keylogger (Safe Demo)** built in Python.  
It records keystrokes locally and demonstrates how such logging works in a controlled, educational setup.  
⚠️ **Note:** This project is strictly for **educational and internship learning purposes only.**

---

## 🔹 Features
- ✅ CLI-based keylogger (no GUI required)  
- ✅ Captures keystrokes in real-time  
- ✅ Sends captured keystrokes to a user-provided **Webhook URL**  
- ✅ Prints banner on startup (for better CLI look)  
- ✅ Runs until **ESC** key is pressed  
- ✅ Lightweight & easy to run in terminal  

---

## 🔹 Requirements
- Python **3.8+**  
- Required libraries (install from `requirements.txt`):  
  - `pynput`  
  - `requests`  

---

## 🔹 Installation & Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/SCT_CS_4_Keylogger_CLI.git
   cd SCT_CS_4_Keylogger_CLI


   pip install -r requirements.txt


python3 keylogger.py



$ python3 keylogger.py
===============================
  CLI Keylogger – Internship Demo
===============================

Enter Webhook URL: https://webhook.site/xxxx-xxxx
Keylogger started. Press ESC to stop.

