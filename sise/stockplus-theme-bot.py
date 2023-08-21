# https://wikidocs.net/185103
# https://stockplus.com/m/investing_strategies/topics/771 맥신 여기서부터 하나씩 늘어남
# pip install python-telegram-bot==13.15

# https://vercel.com/new/templates/python/flask-hello-world

# https://github.com/python-telegram-bot/v13.x-wiki/wiki/Extensions-%E2%80%93-JobQueue

# https://replit.com/@lupin204/PyS07

# https://uptimerobot.com/

import telegram

TOKEN = ''
bot = telegram.Bot(TOKEN)

updates = bot.get_updates()
print(updates[0]['my_chat_member']['chat']['id'])



###

import telegram

TOKEN = 'your token'
ChatId = 'StockPlusThemeBot'
msg = 'hello'

bot = telegram.Bot(TOKEN)
bot.send_message(chat_id=ChatId , text=msg)
