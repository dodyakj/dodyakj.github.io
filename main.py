from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext
import asyncio

# Token bot Telegram Anda
TOKEN = '7205709997:AAHimcCBdO0ywROhCfs6yZjZWAQ0CX0QM78'

# Setup aplikasi bot Telegram
application = Application.builder().token(TOKEN).build()

# Command handler untuk perintah /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_photo(
        photo='https://img.freepik.com/free-photo/digital-painting-fire-letter-d_1340-36092.jpg?ga=GA1.1.1401649289.1691030348&semt=sph',
        caption='Welcome to  Will Of D universe!'
    )
    await update.message.reply_text(
        'Upgrade your coin, earn more coins, boost your ranking, and get more airdrop rewards! \n \n 🎁Play-to-earn airdrop right now!',
        reply_markup={
            'inline_keyboard': [
                [{'text': '🚀 Play Airdrop', 'callback_data': 'game1'}],
                [{'text': 'Join Community', 'callback_data': 'game2'}],
                [{'text': 'Follow Instagram', 'callback_data': 'game3'}],
                [{'text': 'Follow Tiktok', 'callback_data': 'game3'}],
                [{'text': 'Follow Youtube', 'callback_data': 'game3'}],
                [{'text': 'Follow X', 'callback_data': 'game3'}],
            ]
        }
    )


# Callback handler untuk menangani pemilihan game
async def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    game_choice = query.data

    if game_choice == 'game1':
        await query.message.reply_text('Anda memilih Game 1. Memulai Game 1 sekarang...')
    elif game_choice == 'game2':
        await query.message.reply_text('Anda memilih Game 2. Memulai Game 2 sekarang...')
    elif game_choice == 'game3':
        await query.message.reply_text('Anda memilih Game 3. Memulai Game 3 sekarang...')

# Handler untuk pesan yang tidak dikenali
async def unknown(update: Update, context: CallbackContext):
    await update.message.reply_text('Maaf, perintah tidak dikenali. Silakan gunakan /start untuk memulai.')

# Menambahkan handler untuk setiap perintah / command
application.add_handler(CommandHandler('start', start))
application.add_handler(MessageHandler(filters.COMMAND, unknown))
application.add_handler(CallbackQueryHandler(button_callback))  # Use CallbackQueryHandler

# Menjalankan aplikasi polling untuk bot Telegram
application.run_polling()
