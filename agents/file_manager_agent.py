# agents/file_manager_agent.py

import os

def list_files(directory="."):
    try:
        files = os.listdir(directory)
        if not files:
            return "📂 No files found."
        return "📁 Files:\n" + "\n".join(files)
    except Exception as e:
        return f"❌ Error: {str(e)}"

def delete_file(filename):
    try:
        os.remove(filename)
        return f"🗑️ File '{filename}' deleted."
    except Exception as e:
        return f"❌ Failed to delete file: {str(e)}"
