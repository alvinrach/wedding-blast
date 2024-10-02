import pandas as pd
import pywhatkit as kit
import time

# Load CSV file
contacts = pd.read_csv('contacts.csv')

# Function to send WhatsApp message
def send_whatsapp_message(name, phone):
    message = f"Hi, {name}!"
    # You can modify the hour and minute for scheduling the message
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min+1
    kit.sendwhatmsg(f"+{phone}", message, hour, minute)
    print(f"Message sent to {name} at {phone}")

# Loop through each contact and send message
for index, row in contacts.iterrows():
    name = row['name']
    phone = row['phone']
    send_whatsapp_message(name, phone)
    time.sleep(5)  # Adding a delay to avoid sending too many messages quickly
