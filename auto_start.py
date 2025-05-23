# auto_start.py

import subprocess
import sys
import os

def create_task():
    python_path = sys.executable
    script_path = os.path.abspath("main_assistant.py")
    task_name = "SmartAI_Assistant"

    # Create a scheduled task in Windows to run on logon
    cmd = f'schtasks /create /sc onlogon /tn {task_name} /tr "{python_path} {script_path}" /rl highest /f'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("Auto-start task created successfully.")
    else:
        print(f"Failed to create task. Error: {result.stderr}")

if __name__ == "__main__":
    create_task()
