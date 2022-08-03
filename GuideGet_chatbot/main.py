import constants as keys
import responses as R
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Bot started...")

def start_command(update, context):
    update.message.reply_text("Halo! Selamat datang di GuideGet, We Guide You Get :)")

def help_command(update, context):
    update.message.reply_text('Jika Kk butuh bantuan, Kk bisa meminta bantuan Admin Kami.')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_response(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    # Dispatcher 
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
