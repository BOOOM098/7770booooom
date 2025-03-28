# Telegram Text-to-Speech Bot

This is a Telegram bot that converts text messages to speech using Google Text-to-Speech (gTTS).

## Features
- Convert any text message to speech
- Simple and easy to use
- Supports English language
- Sends audio files in MP3 format

## Setup Instructions

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Get a Telegram Bot Token:
   - Open Telegram and search for "@BotFather"
   - Send `/newbot` command
   - Follow the instructions to create your bot
   - Copy the bot token provided by BotFather

3. Configure the bot:
   - Open `text_to_speech_bot.py`
   - Replace `'YOUR_BOT_TOKEN'` with your actual bot token

4. Run the bot:
```bash
python text_to_speech_bot.py
```

## Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to begin
3. Send any text message to convert it to speech
4. The bot will reply with an audio file containing the speech

## Commands
- `/start` - Start the bot
- `/help` - Show help message

## Note
- The bot uses Google Text-to-Speech service, so an internet connection is required
- Audio files are temporarily stored and automatically deleted after sending 