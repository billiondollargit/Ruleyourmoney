import requests
import telebot
import os

# Load API keys from environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

# Initialize Telegram Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    # Call OpenRouter API
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-4o",
            "messages": [{"role": "user", "content": user_input}]
        }
    )

    reply = response.json()['choices'][0]['message']['content']
    bot.reply_to(message, reply)

print("Rule Your Money bot is running...")
bot.polling()
