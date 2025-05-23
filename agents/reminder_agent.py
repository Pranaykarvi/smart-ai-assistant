# agents/reminder_agent.py

import os
import datetime

reminder_file = "data/reminders.txt"
os.makedirs("data", exist_ok=True)

def set_reminder(message):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(reminder_file, "a") as f:
        f.write(f"[{now}] {message}\n")
    return f"📌 Reminder set: '{message}'"

def list_reminders():
    if not os.path.exists(reminder_file):
        return "📝 No reminders yet."
    with open(reminder_file, "r") as f:
        reminders = f.readlines()
    if not reminders:
        return "📝 No reminders yet."
    return "🔔 Your Reminders:\n" + "".join(reminders)
