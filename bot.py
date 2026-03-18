import telebot
from telebot import types
from flask import Flask
from threading import Thread
import os

# --- STEP 1: Flask Server (Isse bot 24/7 zinda rahega) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- STEP 2: Bot Logic ---
# APNA TOKEN YAHAN DALEIN (Secret rakhein!)
API_TOKEN = '8706830781:AAHCJWWhJ_DyuLvQGeGiLrlPGefdf9JjeVg'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('AI')
    btn2 = types.KeyboardButton('Store')
    btn3 = types.KeyboardButton('Media')
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, "🔥 Zyonix Hub mein swagat hai! Niche diye gaye buttons use karein:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    text = message.text.lower()

    if text == "ai":
        bot.reply_to(message, "🚀 Yeh rahi AI ki link: https://zyonixai.xo.je/")
    
    elif text == "store":
        bot.reply_to(message, "🛒 Yeh raha store: https://zyonixstore.xo.je/")

    elif text == "media":
        bot.reply_to(message, "📸 Insta Media Downloader: https://zyonixinstareel.xo.je/")
    
    else:
        bot.reply_to(message, "Samajh nahi aaya! Please buttons use karein ya /start likhein.")

# --- STEP 3: Execution ---
if __name__ == "__main__":
    keep_alive() # Flask starts here
    print("Bot is running...")
    bot.infinity_polling()