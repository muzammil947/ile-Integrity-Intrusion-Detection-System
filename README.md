Smart File Integrity & Intrusion Alert System

A Python-based security tool that monitors files in a selected folder and detects any unauthorized modifications. If a file is changed or tampered with, the system automatically moves it to a quarantine folder and logs the incident with date and time.

This project is designed to demonstrate file integrity monitoring, intrusion detection, and basic cybersecurity concepts using Python.

Features

Register and protect any folder

File integrity verification using SHA-256 hashing

Automatic detection of file tampering

Real-time monitoring of protected files

Automatic quarantine of suspicious files

Security dashboard to view file status

Detailed logs with date and time

Simple Tkinter GUI interface

How It Works

The user selects a folder to protect.

The system generates SHA-256 hash values for all files in that folder.

These hashes are stored in a local database (hash_database.json).

During monitoring, the system recalculates file hashes.

If a hash changes, the file is considered tampered.

The tampered file is moved to the quarantine folder.

The event is recorded in the log file with timestamp.

Project Structure
FileIntegrityChecker
│
├── main.py
├── hash_database.json
├── tamper_logs.txt
├── quarantine/
└── README.md
Technologies Used

Python

Tkinter (GUI)

SHA-256 Hashing

JSON Database

File System Monitoring

Installation

Clone the repository

git clone https://github.com/yourusername/FileIntegrityChecker.git

Go to the project folder

cd FileIntegrityChecker

Run the program

python main.py
Usage

Click Register & Protect Folder to select a folder for monitoring.

Use Scan Integrity (Manual) to check file integrity.

Click Start Real-Time Monitoring to continuously monitor the files.

View the Security Dashboard to see file status.

Check Logs to see detected tampering events.

Example Security Logs
[2026-03-12 10:22:41] C:\protected\data.txt -> TAMPERED & QUARANTINED
Learning Outcomes

This project demonstrates:

File Integrity Monitoring (FIM)

Basic Intrusion Detection Concepts

Cryptographic Hashing

Python GUI Development

Secure File Handling
<img width="857" height="621" alt="Screenshot 2026-03-12 080721" src="https://github.com/user-attachments/assets/9841f1c5-1f77-4225-b3fa-b8089d1c961c" />
