import tkinter as tk
import threading
from agents.automation_agent import handle_task
from voice_utils import listen_command, speak_text  # 👈 Use your module here

# ---------- GUI FUNCTIONS ----------
def process_voice_command():
    output_text.set("🎤 Listening...")
    window.update()

    try:
        command = listen_command()
        if not command:
            output_text.set("❌ Could not recognize speech.")
            return

        command_text.set(command)
        response = handle_task(command)
        output_text.set(response)

        # Speak the response
        speak_text(response)

    except Exception as e:
        output_text.set(f"❌ Error: {str(e)}")

def run_in_thread(func):
    threading.Thread(target=func).start()

def process_text_command():
    command = text_entry.get()
    command_text.set(command)
    response = handle_task(command)
    output_text.set(response)
    speak_text(response)

# ---------- GUI WINDOW ----------
window = tk.Tk()
window.title("🤖 Smart AI Assistant")
window.geometry("600x400")
window.configure(bg="#1e1e1e")

title_label = tk.Label(window, text="Smart AI Assistant", font=("Helvetica", 20, "bold"), fg="#00FFAA", bg="#1e1e1e")
title_label.pack(pady=10)

command_text = tk.StringVar()
output_text = tk.StringVar()

command_label = tk.Label(window, textvariable=command_text, font=("Helvetica", 12), fg="#FFD700", bg="#1e1e1e")
command_label.pack(pady=5)

output_label = tk.Label(window, textvariable=output_text, wraplength=550, font=("Helvetica", 12), fg="#FFFFFF", bg="#1e1e1e")
output_label.pack(pady=10)

# Optional manual entry
text_entry = tk.Entry(window, width=50, font=("Helvetica", 12))
text_entry.pack(pady=5)

# ---------- BUTTONS ----------
button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=10)

speak_button = tk.Button(button_frame, text="🎤 Speak", font=("Helvetica", 12), command=lambda: run_in_thread(process_voice_command), bg="#0078D7", fg="white", width=10)
speak_button.grid(row=0, column=0, padx=10)

text_button = tk.Button(button_frame, text="📩 Send", font=("Helvetica", 12), command=process_text_command, bg="#28A745", fg="white", width=10)
text_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="❌ Exit", font=("Helvetica", 12), command=window.quit, bg="#DC3545", fg="white", width=10)
exit_button.grid(row=0, column=2, padx=10)

# ---------- MAIN LOOP ----------
window.mainloop()
