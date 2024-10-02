import pandas as pd
import pyautogui
import time
import webbrowser
import urllib.parse

# Load CSV file
contacts = pd.read_csv('contacts.csv')

webbrowser.open(f"https://web.whatsapp.com")
time.sleep(10)  # Wait for WhatsApp Web to load
pyautogui.hotkey('ctrl', '0')

# Function to send WhatsApp message
def send_whatsapp_message(name, phone):
    message = f"Do you mind, {name}!"
    pyautogui.click(588, 479)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(str(phone))
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(1440, 1730)
    pyautogui.write(message)
    pyautogui.press('enter')
    time.sleep(1)
    print(f"Message sent to {name} at {phone}")

# Loop through each contact and send message
for index, row in contacts.iterrows():
    name = row['name']
    phone = row['phone']
    send_whatsapp_message(name, phone)