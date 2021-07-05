from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
from datetime import date
import requests
from requests.exceptions import Timeout

TOKEN='1885665222:AAGQFu9XXuhvKCAuos9SRMoc0bw8_LMMyQs'
updater = Updater(token=TOKEN,use_context=True)
dispatcher = updater.dispatcher

def hello(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Hello, World')

def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Welcome to CoPandemicInfoBot,Get info about covid19!')

def presentDate(update,context):
    todaysdate = date.today()
    today = todaysdate.strftime("%B %d, %Y")
    context.bot.send_message(chat_id=update.effective_chat.id,text=today)

# function for summary
def summary(update,context):
    # session = requests.Session()
    response = requests.get('https://api.covid19api.com/summary')
    if response.status_code == 200:
        json_response = response.json()
        global_data = json_response['Global']
        todaysdate = date.today()
        today = todaysdate.strftime("%B %d, %Y")
        summary_data = f"Covid 19 Summary (as of {today})\nNew Confirmed : {global_data['NewConfirmed']}\nTotal Confirmed : {global_data['TotalConfirmed']}\nNew Deaths : {global_data['NewDeaths']}\nTotal Deaths : {global_data['TotalDeaths']}\nNew Recovered : {global_data['NewRecovered']}\nTotal Recovered : {global_data['TotalRecovered']}"
        context.bot.send_message(chat_id=update.effective_chat.id,text=summary_data)
    else :
        context.bot.send_message(chat_id=update.effective_chat.id,text="Not 200 response code")

# for unknow commands 
def unknown(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Sorry, I didnt understand that command')

# use of CommandHandler and register it in dispatcher. Linking the /hello command with the function hello()
hello_handler = CommandHandler('hello',hello)
start_handler = CommandHandler('start',start)
date_handler = CommandHandler('date',presentDate)
corona_summary_handler = CommandHandler('summary',summary)
unknown_handler = MessageHandler(Filters.command,unknown)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(date_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(corona_summary_handler)
dispatcher.add_handler(unknown_handler)
# To start the bot 
updater.start_polling()
