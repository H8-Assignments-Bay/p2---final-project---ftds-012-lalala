import pickle
import json
import string
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.update import Update
import numpy as np
from util import JSONParser

#Load json file
jp = JSONParser()
jp.parse('data/intents.json')
df = jp.get_dataframe()

# Load model

model = pickle.load(open("model_chatbot.pkl", "rb"))
   
def preprocess(chat):
    # konversi ke non kapital
    chat = chat.lower()
    # hilangkan tanda baca
    tandabaca = tuple(string.punctuation)
    chat = ''.join(ch for ch in chat if ch not in tandabaca)
    return chat

def bot_response(chat, pipeline, jp):
    chat = preprocess(chat)
    res = pipeline.predict_proba([chat])
    max_prob = max(res[0])
    if max_prob < 0.2:
        return "Maaf ya Ka, Gege belum ngerti :(" , None
    else:
        max_id = np.argmax(res[0])
        pred_tag = pipeline.classes_[max_id]
        return jp.get_response(pred_tag), pred_tag
    


global TOKEN 

TOKEN  = "5512871990:AAGglYMFnssDyysG2kMEw3BgySTBiRpcEj0"


print("Bot started...")

def start_command(update: Update , context: CallbackContext):
    update.message.reply_text("Halo! Selamat datang di GuideGet")

def help_command(update, context: CallbackContext):
    update.message.reply_text('Jika kamu butuh bantuan, kamu bisa meminta bantuan Admin kami.')

def reply(update, context):
    user_input = str(update.message.text)
    update.message.reply_text(bot_response(user_input, model, jp)[0])
    
def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    # Dispatcher 
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, reply))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()   