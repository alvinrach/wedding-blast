import pandas as pd
import pyautogui
import time
import webbrowser
import urllib.parse

# Load CSV file
contacts = pd.read_csv('contacts.csv')

# Function to send WhatsApp message
def send_whatsapp_message(name, phone):
    message = f"Hi, {name}!"
    # URL encode the message
    encoded_message = urllib.parse.quote(message)
    
    # Open WhatsApp Web with the encoded message
    webbrowser.open(f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}")
    time.sleep(9)  # Wait for WhatsApp Web to load

    # Press Enter to send the message
    pyautogui.press('enter')
    print(f"Message sent to {name} at {phone}")

    # Close the tab
    time.sleep(2)  # Optional: Wait a moment before closing the tab
    pyautogui.hotkey('ctrl', 'w')  # Use 'cmd' for macOS

# Loop through each contact and send message
for index, row in contacts.iterrows():
    name = row['name']
    phone = row['phone']
    send_whatsapp_message(name, phone)
    # time.sleep(5)  # Adding a delay to avoid sending too many messages quickly
