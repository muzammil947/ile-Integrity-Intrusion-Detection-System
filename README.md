# 🔐 Smart File Integrity & Intrusion Alert System

## 📌 Overview

A Python-based security tool that monitors files within a selected folder and detects unauthorized modifications. If any file is altered or tampered with, the system automatically isolates it in a quarantine folder and logs the event with a timestamp.

This project demonstrates core cybersecurity concepts such as file integrity monitoring, intrusion detection, and automated response mechanisms.

---

## 🚀 Features

* 📁 Register and monitor any folder
* 🔑 File integrity verification using SHA-256 hashing
* ⚠️ Automatic detection of file tampering
* 🔄 Real-time monitoring of protected files
* 🛑 Automatic quarantine of suspicious files
* 📊 Security dashboard for file status tracking
* 📝 Detailed logs with date and time
* 🖥️ User-friendly GUI built with Tkinter

---

## ⚙️ How It Works

1. The user selects a folder to protect
2. The system generates SHA-256 hash values for all files
3. Hashes are stored in a local JSON database (`hash_database.json`)
4. During monitoring, hashes are recalculated
5. If a mismatch is detected, the file is flagged as tampered
6. The file is moved to the `quarantine/` folder
7. The event is logged with a timestamp in `tamper_logs.txt`

---

## 📁 Project Structure

```
FileIntegrityChecker/
│── main.py
│── hash_database.json
│── tamper_logs.txt
│── quarantine/
│── README.md
```

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* SHA-256 Hashing
* JSON (for lightweight database)
* File System Operations

---

## 💻 Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/FileIntegrityChecker.git
```

### 2. Navigate to the project directory

```
cd FileIntegrityChecker
```

### 3. Run the application

```
python main.py
```

---

## ▶️ Usage

* Click **"Register & Protect Folder"** to select a folder
* Use **"Scan Integrity (Manual)"** to verify file status
* Click **"Start Real-Time Monitoring"** for continuous protection
* View the **Security Dashboard** for file status
* Check **Logs** to see tampering events

---

## 🎯 Key Learning Outcomes

* Implemented file integrity verification using cryptographic hashing
* Designed a real-time monitoring system for intrusion detection
* Built a GUI-based security tool for non-technical users
* Applied practical cybersecurity concepts in a real-world scenario

---


---

Example Security Logs
[2026-03-12 10:22:41] C:\protected\data.txt -> TAMPERED & QUARANTINED
Learning Outcomes
## 🏁 Conclusion

This project highlights how Python can be used to build lightweight security tools for monitoring file integrity and detecting unauthorized access, making it useful for basic system protection and educational purposes.

<img width="857" height="621" alt="Screenshot 2026-03-12 080721" src="https://github.com/user-attachments/assets/9841f1c5-1f77-4225-b3fa-b8089d1c961c" />
