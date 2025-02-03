# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | @NT_BOTS_SUPPORT | LISA-KOREA/UPLOADER-BOT-V4

from flask import Flask
from threading import Thread
import os
from plugins.config import Config
from pyrogram import Client

# יצירת שרת Flask פשוט להאזנה על הפורט
app = Flask(__name__)

@app.route('/')
def home():
    return "🎊 Bot is alive! 🎊"

def run_flask():
    app.run(host='0.0.0.0', port=8000)

if __name__ == "__main__":
    # הפעלת שרת Flask ברקע
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # הפעלת הבוט של טלגרם
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Client = Client(
        "@UploaderXNTBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=300,
        plugins=plugins
    )
    print("🎊 I AM ALIVE 🎊  • Support @NT_BOTS_SUPPORT")
    Client.run()
