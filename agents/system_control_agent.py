# agents/system_control_agent.py
import os
import webbrowser

def open_file_explorer():
    os.system("explorer")  # Windows only
    return "Opening File Explorer..."

def open_browser_with_url(url):
    webbrowser.open(url)
    return f"Opening {url}..."

def shutdown():
    return "Shutdown command sent."

def restart():
    return "Restart command sent."

def sleep():
    return "Sleep command sent."
