# agents/reminder_agent.py
reminders = []

def save_reminder(text):
    reminders.append(text)
    return f"✅ Reminder saved: {text}"

def list_reminders():
    return "\n".join(f"🔔 {r}" for r in reminders) if reminders else "📭 No reminders yet."
