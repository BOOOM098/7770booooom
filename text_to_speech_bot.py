import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from gtts import gTTS
import tempfile
import asyncio
import sys

# Set event loop policy for Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Your Telegram bot token
TOKEN = '7720492883:AAEKv88ULrgRI2zyLF9REoyxLwRtuHUxdu4'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Text-to-Speech Bot! 👋\n\n"
        "Just send me any text message and I'll convert it to speech for you.\n"
        "Use /help to see available commands."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n\n"
        "Just send any text message to convert it to speech!"
    )

async def text_to_speech(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    # Create a temporary file to store the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
        # Convert text to speech
        tts = gTTS(text=text, lang='en')
        tts.save(temp_file.name)
        
        # Send the audio file
        await update.message.reply_audio(
            audio=open(temp_file.name, 'rb'),
            title="Text to Speech",
            performer="Text-to-Speech Bot"
        )
        
        # Clean up the temporary file
        os.unlink(temp_file.name)

def main():
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_to_speech))

    # Start the bot
    print("Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Bot stopped by user")
        sys.exit(0) ped by user")
        sys.exit(0) 