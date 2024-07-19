from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import asyncio

# Token bot Telegram Anda
TOKEN = '7205709997:AAHimcCBdO0ywROhCfs6yZjZWAQ0CX0QM78'

# URL aplikasi web game Web3 Anda
WEB3_GAME_URL = 'https://will-of-d-0tpv2.kinsta.page'

# Setup aplikasi bot Telegram
application = Application.builder().token(TOKEN).build()

# Command handler untuk perintah /start
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton('🚀 Play Airdrop', web_app=dict(url=WEB3_GAME_URL))],
        [InlineKeyboardButton('Join Community', url='https://t.me/will_of_d_official')],
        [InlineKeyboardButton('Follow Instagram', url='https://www.instagram.com/yourprofile')],
        [InlineKeyboardButton('Follow Tiktok', url='https://www.tiktok.com/@yourprofile')],
        [InlineKeyboardButton('Follow Youtube', url='https://www.youtube.com/@will_ofD')],
        [InlineKeyboardButton('Follow X', url='https://x.com/yourprofile')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        await update.message.reply_photo(
            photo='https://img.freepik.com/free-photo/digital-painting-fire-letter-d_1340-36092.jpg?ga=GA1.1.1401649289.1691030348&semt=sph',
            caption='Welcome to Will Of D universe!',
        )
        await update.message.reply_text(
            'Upgrade your coin, earn more coins, boost your ranking, and get more airdrop rewards! \n \n 🎁Play-to-earn airdrop right now!',
            reply_markup=reply_markup
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        await update.message.reply_text("An error occurred while processing your request. Please try again later.")

# Handler untuk pesan yang tidak dikenali
async def unknown(update: Update, context: CallbackContext):
    await update.message.reply_text('Maaf, perintah tidak dikenali. Silakan gunakan /start untuk memulai.')

# Menambahkan handler untuk setiap perintah / command
application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.COMMAND, unknown))

if __name__ == '__main__':
    application.run_polling()
