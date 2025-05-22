import os
import re
import webbrowser
from textblob import TextBlob

# Set path to Brave
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

APP_SHORTCUTS = {
    "vs code": "code",
    "notepad": "notepad",
    "calculator": "calc",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "brave": BRAVE_PATH,
    "file explorer": r"explorer.exe",  # Added file explorer
}

def autocorrect(text):
    corrected = str(TextBlob(text).correct())
    return corrected

def normalize_command(command: str) -> str:
    command = command.lower().strip()

    # Remove filler words like 'app', 'application'
    command = command.replace(" app", "").replace(" application", "")

    command = command.replace(" slash ", "/").replace("slash", "/")
    command = command.replace(" dot ", ".").replace(" dot", ".").replace("dot ", ".")

    # Combine phrases like 'chat gpt com' -> 'chatgpt.com'
    domain_match = re.search(r"\b([a-z0-9]+)\s+([a-z0-9]+)\s+com\b", command)
    if domain_match:
        combined = domain_match.group(1) + domain_match.group(2) + ".com"
        command = re.sub(r"\b[a-z0-9]+\s+[a-z0-9]+\s+com\b", combined, command)

    return command.strip()

def clean_url(url: str) -> str:
    url = url.replace(" ", "")
    if not url.startswith("http"):
        url = "https://" + url
    return url

def handle_task(raw_command: str) -> str:
    # Skip autocorrect if URLs/domains present or app commands
    skip_autocorrect = any(
        keyword in raw_command.lower()
        for keyword in [".com", "/", "slash", "dot", "open", "github", "youtube", "app", "application"]
    )

    if skip_autocorrect:
        command = raw_command
    else:
        command = autocorrect(raw_command)

    command = normalize_command(command)

    try:
        brave = webbrowser.get(f'"{BRAVE_PATH}" %s')

        # 🌐 CASE 1: Open site and search something (e.g. "open youtube.com and search for AI")
        if "open" in command and "search for" in command:
            match = re.search(r"open\s+(.*?)\s+(?:and)?\s*search\s+for\s+(.+)", command)
            if match:
                site, query = match.groups()
                site = site.strip().replace(" ", "")
                query = query.strip().replace(" ", "+")

                if "youtube" in site:
                    url = f"https://www.youtube.com/results?search_query={query}"
                elif "google" in site:
                    url = f"https://www.google.com/search?q={query}"
                else:
                    url = f"https://{site}/search?q={query}"

                brave.open(url)
                return f"🔍 Searching '{query.replace('+', ' ')}' on {site.title()}"

        # 🌐 CASE 2: Direct website open (e.g. "open github.com/pranaykarvi")
        if "open" in command:
            url = command.split("open", 1)[1].strip()
            # If this looks like an app name (no dot or slash), skip URL open and try app launch below
            if ('.' not in url and '/' not in url):
                pass
            else:
                url = clean_url(url)
                brave.open(url)
                return f"🌐 Opening {url} in Brave..."

        # ⚙️ CASE 3: Launch apps (improved matching)
        for app, path in APP_SHORTCUTS.items():
            # Check if all words in app name appear in command (for flexible matching)
            if all(word in command for word in app.split()):
                os.startfile(path)
                return f"✅ Launching {app.title()}..."

        # 🔎 CASE 4: Smart search like "search AI agents on youtube"
        match = re.search(r"(?:search|find)\s+(.*?)\s+(?:on|in)\s+(\S+)", command)
        if match:
            query, site = match.groups()
            site = site.strip()
            query = query.strip().replace(" ", "+")

            if "youtube" in site:
                url = f"https://www.youtube.com/results?search_query={query}"
            elif "google" in site:
                url = f"https://www.google.com/search?q={query}"
            else:
                url = f"https://{site}/search?q={query}"

            brave.open(url)
            return f"🔍 Searching '{query.replace('+', ' ')}' on {site.title()}"

        # 🔎 CASE 5: Fallback Google Search
        fallback_query = raw_command.replace(" ", "+")
        url = f"https://www.google.com/search?q={fallback_query}"
        brave.open(url)
        return f"🤖 Couldn't recognize the command, searching Google for: '{raw_command}'"

    except Exception as e:
        return f"❌ Error handling command: {str(e)}"
