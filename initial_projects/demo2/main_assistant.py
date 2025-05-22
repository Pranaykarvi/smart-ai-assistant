import time
from voice_utils import listen_command, text_to_speech
from helper import normalize_command

from agents import (
    weather_agent,
    translator_agent,
    summarizer_agent,
    coder_agent,
    reminder_agent,
    info_agent,
    automation_agent
)

def greet_user():
    greeting = "Smart AI Assistant started. Say something!"
    print(greeting)
    text_to_speech(greeting)

def route_command(command: str) -> str:
    command = command.lower()

    if "weather" in command:
        return weather_agent.handle_task(command)
    elif "translate" in command:
        return translator_agent.handle_task(command)
    elif "summarize" in command:
        return summarizer_agent.handle_task(command)
    elif "code" in command or "generate code" in command:
        return coder_agent.handle_task(command)
    elif "remind" in command or "reminder" in command:
        return reminder_agent.handle_task(command)
    elif "time" in command or "date" in command:
        return info_agent.handle_task(command)
    elif "open" in command or "search" in command or "." in command:
        return automation_agent.handle_task(command)
    else:
        return info_agent.handle_task(command)

def main():
    greet_user()
    while True:
        try:
            print("\nListening for your command...")
            command = listen_command()

            if not command:
                print("Recognition error or no input detected.")
                continue

            print(f"Command received: {command}")
            command = normalize_command(command)
            print(f"Normalized: {command}")
            
            response = route_command(command)
            print(f"Response: {response}")
            text_to_speech(response)

            time.sleep(1)

        except KeyboardInterrupt:
            print("\n🛑 Exiting Smart AI Assistant. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            text_to_speech("Something went wrong. Please try again.")
            continue

if __name__ == "__main__":
    main()
