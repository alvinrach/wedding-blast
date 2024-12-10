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
def send_whatsapp_message(name, title, phone):
    encoded_name = urllib.parse.quote(name)
    message = (
        f"Kepada Yth. \n"
        f"{title}\n"
        f"{name}\n"
        f"____\n\n"
        "‎اللهِ الرَّحْمَنِ الرَّحِيْم‎‎ بِسْــــــــــــــــــمِ\n\n"
        "Assalamu'alaikum Warahmatullahi Wabarakaatuh\n\n"
        "Tanpa mengurangi rasa hormat, perkenankan kami mengundang Bapak/Ibu/Saudara/i, teman sekaligus sahabat, "
        "untuk menghadiri acara pernikahan kami:\n\n"
        "Alvio Yunita Putri, S.T\n"
        "&\n"
        "Alvin Rachmat, S.T\n\n"
        "yang InsyaAllah akan diselenggarakan pada :\n\n"
        "Akad & Resepsi di Palembang\n"
        "Hari, tanggal    : Minggu, 27 Oktober 2024\n"
        "Waktu            : 10:00 WIB s.d. Selesai\n"
        "Tempat           : Kediaman mempelai wanita di Palembang\n\n"
        "Resepsi (Tueng Dara Baro) di Banda Aceh\n"
        "Hari, tanggal    : Minggu, 17 November 2024\n"
        "Waktu            : 11:30 WIB s.d. Selesai\n"
        "Tempat           : Gedung Hj. Yusriah di Banda Aceh\n\n"
        f"Berikut link untuk info lengkap dari acara kami :\n"
        f"https://foreverr.id/alvioalvin/?to={encoded_name}\n\n"
        "Merupakan suatu kebahagiaan bagi kami apabila Bapak/Ibu/Saudara/i berkenan untuk hadir dan memberikan doa restu.\n\n"
        "Mohon maaf perihal undangan hanya dibagikan melalui pesan ini dikarenakan keterbatasan jarak dan waktu.\n\n"
        "Wassalamu'alaikum Warahmatullahi Wabarakaatuh\n\n"
        "Terima Kasih..\n\n"
        "Hormat kami,\n"
        "Alvio & Alvin"
    )
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
    title = row['title']
    phone = row['phone']
    send_whatsapp_message(name, title, phone)