import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import os
import json
import shutil
from datetime import datetime

# ---------------- CONFIG ----------------
HASH_DB = "hash_database.json"
LOG_FILE = "tamper_logs.txt"
QUARANTINE_DIR = "quarantine"

if not os.path.exists(QUARANTINE_DIR):
    os.mkdir(QUARANTINE_DIR)

# ---------------- UTILITY FUNCTIONS ----------------

def sha256_hash(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()


def load_db():
    if os.path.exists(HASH_DB):
        with open(HASH_DB, 'r') as f:
            return json.load(f)
    return {}


def save_db(db):
    with open(HASH_DB, 'w') as f:
        json.dump(db, f, indent=4)


def log_event(file, status):
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{datetime.now()}] {file} -> {status}\n")


# ---------------- CORE FUNCTIONS ----------------

def register_folder():
    folder = filedialog.askdirectory()
    if not folder:
        return

    db = {}
    for root_, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root_, file)
            try:
                db[path] = sha256_hash(path)
            except:
                pass

    save_db(db)
    messagebox.showinfo(
        "Success",
        "Folder registered & protected successfully!"
    )


def quarantine(file):
    if os.path.exists(file):
        dest = os.path.join(
            QUARANTINE_DIR,
            os.path.basename(file)
        )
        try:
            shutil.move(file, dest)
            os.chmod(dest, 0o444)  # Read-only lock
        except:
            pass


def monitor_folder():
    db = load_db()
    if not db:
        messagebox.showwarning(
            "No Data",
            "No folder registered!"
        )
        return

    alert = False

    for file, old_hash in db.items():
        if os.path.exists(file):
            try:
                new_hash = sha256_hash(file)
                if new_hash != old_hash:
                    alert = True
                    quarantine(file)
                    log_event(file, "TAMPERED & QUARANTINED")
            except:
                pass

    if alert:
        messagebox.showerror(
            "🚨 INTRUSION ALERT",
            "Tampering detected!\nFile moved to quarantine."
        )
    else:
        messagebox.showinfo(
            "System Safe",
            "All files are intact."
        )


def realtime_monitor():
    monitor_folder()
    root.after(10000, realtime_monitor)  # Every 10 seconds


def view_dashboard():
    dash = tk.Toplevel(root)
    dash.title("Security Dashboard")
    dash.geometry("600x400")

    text = tk.Text(dash, bg="#020617", fg="#38bdf8")
    text.pack(expand=True, fill=tk.BOTH)

    db = load_db()
    for file in db:
        status = "SAFE"
        if not os.path.exists(file):
            status = "QUARANTINED / REMOVED"
        text.insert(
            tk.END,
            f"{file}  --->  {status}\n"
        )


def view_logs():
    if not os.path.exists(LOG_FILE):
        messagebox.showinfo("Logs", "No logs available")
        return

    win = tk.Toplevel(root)
    win.title("Security Logs")
    win.geometry("500x300")

    t = tk.Text(win)
    t.pack(expand=True, fill=tk.BOTH)

    with open(LOG_FILE) as f:
        t.insert(tk.END, f.read())


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Smart File Integrity & Intrusion Alert System")
root.geometry("700x500")
root.configure(bg="#020617")

header = tk.Label(
    root,
    text="Smart File Integrity & Intrusion Alert System",
    font=("Segoe UI", 18, "bold"),
    bg="#020617",
    fg="#38bdf8"
)
header.pack(pady=20)

btn_cfg = {
    "font": ("Segoe UI", 12),
    "width": 35,
    "bg": "#0ea5e9",
    "fg": "black"
}

tk.Button(
    root,
    text="Register & Protect Folder",
    command=register_folder,
    **btn_cfg
).pack(pady=8)

tk.Button(
    root,
    text="Scan Integrity (Manual)",
    command=monitor_folder,
    **btn_cfg
).pack(pady=8)

tk.Button(
    root,
    text="Start Real-Time Monitoring",
    command=realtime_monitor,
    **btn_cfg
).pack(pady=8)

tk.Button(
    root,
    text="View Security Dashboard",
    command=view_dashboard,
    **btn_cfg
).pack(pady=8)

tk.Button(
    root,
    text="View Logs",
    command=view_logs,
    **btn_cfg
).pack(pady=8)

tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    font=("Segoe UI", 12),
    width=35,
    bg="#ef4444",
    fg="white"
).pack(pady=25)

root.mainloop()
