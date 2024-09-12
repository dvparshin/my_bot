import os
import ephem
from datetime import datetime
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуй, пользователь!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def planet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        planet_name = ' '.join(context.args).capitalize()
        today = datetime.now(tz=None).strftime('%Y/%m/%d')
        planet = getattr(ephem, planet_name)(today)
        constellation = ephem.constellation(planet)
    except AttributeError:
        constellation = "Нет такой планеты"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=constellation)

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.environ['API_KEY']).build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    planet_handler = CommandHandler('planet', planet)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(planet_handler)

    application.run_polling()