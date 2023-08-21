# https://stockplus.com/m/investing_strategies/topics/771 맥신 여기서부터 하나씩 늘어남

# https://vercel.com/new/templates/python/flask-hello-world

# https://github.com/python-telegram-bot/v13.x-wiki/wiki/Extensions-%E2%80%93-JobQueue

# https://replit.com/@lupin204/PyS07

# https://uptimerobot.com/

import telegram
import asyncio

from datetime import datetime


TOKEN = '6363791280:AAEkRY1l6OyB_DrGKOvmSZ6EBkW2SU56SBk'
ChatId = '6578669349'

current_time = datetime.now().strftime("%H:%M:%S")
msg = f'[{current_time}] hello'

bot = telegram.Bot(token=TOKEN)

asyncio.run(bot.send_message(chat_id=ChatId , text=msg))
    
updates = asyncio.run(bot.get_updates())

    
    


