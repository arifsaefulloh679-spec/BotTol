import telebot, requests, os
BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_KEY = os.getenv("GROQ_KEY")
bot = telebot.TeleBot(BOT_TOKEN)
def tanya(q):
    r = requests.post("https://api.groq.com/openai/v1/chat/completions", headers={"Authorization": f"Bearer {GROQ_KEY}"}, json={"model": "openai/gpt-oss-20b", "messages": [{"role": "system", "content": "Kamu BotTol, teman gaul jawab santai pake Don"}, {"role": "user", "content": q}]}, timeout=60)
    return r.json()['choices'][0]['message']['content']
@bot.message_handler(func=lambda m: True)
def balas(m):
    bot.reply_to(m, tanya(m.text))
print("BOT JADI")
bot.infinity_polling()
